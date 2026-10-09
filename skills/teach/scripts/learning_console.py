#!/usr/bin/env python3
import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

STATES = ["unseen", "exposed", "practiced", "verified", "durable"]
RANK = {name: index for index, name in enumerate(STATES)}
WEAK_WORDS = ("失败", "错误", "不会", "不确定", "提示", "incorrect", "failed", "wrong", "hint")


def default_state_root() -> Path:
    if os.environ.get("TEACH_STATE_HOME"):
        return Path(os.environ["TEACH_STATE_HOME"])
    if os.name == "nt" and os.environ.get("LOCALAPPDATA"):
        return Path(os.environ["LOCALAPPDATA"]) / "TeachSkill"
    if os.environ.get("XDG_STATE_HOME"):
        return Path(os.environ["XDG_STATE_HOME"]) / "teach-skill"
    return Path.home() / ".local" / "state" / "teach-skill"


def read_json(path: Path, fallback):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return fallback


def normalize_action(query: str) -> str:
    value = (query or "").strip()
    value = re.sub(r"^\$teach\b", "", value, flags=re.I).strip()
    if not value:
        return "home"
    rules = [
        ("continue", ("继续", "接着学", "上次课程", "上次学习")),
        ("start", ("开始", "体验", "开始学习")),
        ("progress", ("进度", "学习情况", "掌握情况")),
        ("knowledge", ("知识点", "知识地图", "课程大纲", "有哪些内容", "学什么")),
        ("review", ("复习", "薄弱", "巩固", "错题")),
        ("help", ("帮助", "怎么用", "用法", "指令")),
        ("courses", ("课程列表", "有哪些课程", "已安装课程", "查看课程", "课程")),
    ]
    lowered = value.casefold()
    for action, phrases in rules:
        if any(phrase in lowered for phrase in phrases):
            return action
    return "unknown"


def load_courses(root: Path, state_root: Path):
    courses = []
    if not root.exists():
        return courses
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        manifest = read_json(directory / "course.yaml", None)
        graph = read_json(directory / "graph.yaml", None)
        if not isinstance(manifest, dict) or not isinstance(graph, dict) or not manifest.get("id"):
            continue
        course_id = manifest["id"]
        state = read_json(state_root / f"{course_id}.json", {"schema_version": 1, "course_id": course_id, "nodes": {}})
        if not isinstance(state.get("nodes"), dict):
            state["nodes"] = {}
        courses.append({"id": course_id, "path": directory, "manifest": manifest, "graph": graph, "state": state})
    return courses


def course_summary(course):
    manifest = course["manifest"]
    return {
        "id": course["id"],
        "title": manifest.get("title", course["id"]),
        "version": manifest.get("version", "unknown"),
        "status": manifest.get("status", "unknown"),
        "intended_use": manifest.get("intended_use"),
        "review_required": bool(manifest.get("review_required")),
        "has_history": bool(course["state"]["nodes"]),
        "node_count": len(course["graph"].get("nodes", [])),
    }


def parse_time(value):
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def course_metrics(course, now):
    graph_nodes = course["graph"].get("nodes", [])
    state_nodes = course["state"]["nodes"]
    ids = [node.get("id") for node in graph_nodes if node.get("id")]
    titles = {node.get("id"): node.get("title", node.get("id")) for node in graph_nodes}
    order = [item for item in course["manifest"].get("suggested_order", ids) if item in titles]
    order += [item for item in ids if item not in order]
    counts = Counter()
    due, weak = [], []
    for node_id in ids:
        item = state_nodes.get(node_id, {})
        status = item.get("status", "unseen")
        if status not in RANK:
            status = "unseen"
        counts[status] += 1
        due_at = parse_time(item.get("review_due"))
        if due_at and due_at <= now and status != "unseen":
            due.append(node_id)
        note = str(item.get("note", "")).casefold()
        attempts = int(item.get("attempts", 0) or 0)
        if RANK[status] < RANK["verified"] and (attempts >= 2 or any(word in note for word in WEAK_WORDS)):
            weak.append(node_id)
    updates = []
    for node_id, item in state_nodes.items():
        if node_id in titles:
            updated = parse_time(item.get("updated_at"))
            if updated:
                updates.append((updated, node_id))
    last_id = max(updates)[1] if updates else None
    status_by_id = {}
    for node_id in ids:
        status = state_nodes.get(node_id, {}).get("status", "unseen")
        status_by_id[node_id] = status if status in RANK else "unseen"
    prerequisites = {node.get("id"): node.get("prerequisites", []) for node in graph_nodes}
    eligible = [node_id for node_id in order if all(RANK.get(status_by_id.get(dep, "unseen"), 0) >= RANK["verified"] for dep in prerequisites.get(node_id, []))]
    recommended, reason = None, None
    for candidates, why in ((due, "到期复习"), (weak, "薄弱证据"),
                            ([item for item in eligible if status_by_id.get(item, "unseen") == "unseen"], "新的可学习节点"),
                            ([item for item in eligible if RANK.get(status_by_id.get(item, "unseen"), 0) < RANK["durable"]], "继续巩固")):
        ordered = [item for item in order if item in candidates]
        if ordered:
            recommended, reason = ordered[0], why
            break
    return {
        "counts": {state: counts.get(state, 0) for state in STATES},
        "last_node": ({"id": last_id, "title": titles[last_id], "status": status_by_id[last_id]} if last_id else None),
        "due": [{"id": item, "title": titles[item], "status": status_by_id[item]} for item in due],
        "weak": [{"id": item, "title": titles[item], "status": status_by_id[item]} for item in weak],
        "recommended": ({"id": recommended, "title": titles[recommended], "reason": reason,
                         "status": status_by_id[recommended]} if recommended else None),
        "status_by_id": status_by_id,
        "titles": titles,
        "order": order,
        "prerequisites": prerequisites,
    }


def knowledge_groups(course, metrics):
    source_map = read_json(course["path"] / "source-map.yaml", {"mappings": []})
    starts = {item.get("node_id"): item.get("start_line") for item in source_map.get("mappings", [])}
    try:
        lines = (course["path"] / "source.md").read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    groups, current = [], None
    for node_id in metrics["order"]:
        line_number = starts.get(node_id)
        heading_level = None
        if isinstance(line_number, int) and 1 <= line_number <= len(lines):
            match = re.match(r"^(#{1,6})\s+", lines[line_number - 1])
            heading_level = len(match.group(1)) if match else None
        if current is None or heading_level == 1:
            current = {"id": f"group-{len(groups) + 1}", "title": metrics["titles"][node_id], "nodes": []}
            groups.append(current)
        current["nodes"].append(node_id)
    if not groups and metrics["order"]:
        groups = [{"id": "group-1", "title": "课程内容", "nodes": list(metrics["order"])}]
    result = []
    for group in groups:
        statuses = Counter(metrics["status_by_id"].get(node_id, "unseen") for node_id in group["nodes"])
        result.append({
            "id": group["id"], "title": group["title"], "node_count": len(group["nodes"]),
            "verified_or_durable": statuses.get("verified", 0) + statuses.get("durable", 0),
            "nodes": group["nodes"],
        })
    return result


def select_course(courses, course_id):
    if course_id:
        return next((course for course in courses if course["id"] == course_id), None)
    return courses[0] if len(courses) == 1 else None


def build_result(action, courses, course_id, group_id, now):
    summaries = [course_summary(course) for course in courses]
    if action == "help":
        return {"view": "help", "action": action, "courses": summaries,
                "next_options": ["$teach", "$teach 开始", "$teach 进度", "$teach 课程", "$teach 知识点", "$teach 复习"]}
    if action == "courses":
        return {"view": "courses", "action": action, "courses": summaries,
                "next_options": ["选择一门课程", "$teach", "$teach 帮助"]}
    if not courses:
        return {"view": "no_courses", "action": action, "courses": [],
                "next_options": ["$teach 帮助"]}
    course = select_course(courses, course_id)
    if course_id and not course:
        return {"view": "invalid_course", "action": action, "requested_course": course_id,
                "courses": summaries, "next_options": ["选择一门课程", "$teach 课程"]}
    if not course:
        return {"view": "choose_course", "action": action, "courses": summaries,
                "next_options": ["选择一门课程", "$teach 课程"]}
    summary = course_summary(course)
    metrics = course_metrics(course, now)
    common = {"action": action, "course": summary, "metrics": metrics}
    if action == "home":
        common.update({"view": "returning_home" if summary["has_history"] else "new_home",
                       "next_options": (["继续学习", "复习薄弱部分", "查看学习进度", "查看知识地图"] if summary["has_history"]
                                        else ["开始 5 分钟体验", "查看课程知识地图", "查看学习进度", "使用帮助"])})
        return common
    if action == "progress":
        common.update({"view": "progress", "next_options": ["继续学习", "复习", "查看知识地图"]})
        return common
    if action == "knowledge":
        groups = knowledge_groups(course, metrics)
        selected = next((item for item in groups if item["id"] == group_id), None) if group_id else None
        if selected:
            selected = dict(selected)
            selected["nodes"] = [{"id": node_id, "title": metrics["titles"][node_id],
                                  "status": metrics["status_by_id"][node_id],
                                  "prerequisites": metrics["prerequisites"].get(node_id, [])} for node_id in selected["nodes"]]
        common.update({"view": "knowledge", "grouping_basis": "source_h1_then_order",
                       "groups": [{k: v for k, v in item.items() if k != "nodes"} for item in groups],
                       "selected_group": selected,
                       "next_options": ["展开一个分组", "继续学习", "查看学习进度"]})
        return common
    if action == "review":
        if metrics["due"]:
            review_kind, candidates = "due", metrics["due"]
        elif metrics["weak"]:
            review_kind, candidates = "weak", metrics["weak"]
        else:
            review_kind, candidates = "none", []
        common.update({"view": "review", "review_kind": review_kind, "review_candidates": candidates,
                       "next_options": (["开始复习", "查看进度", "继续学习"] if candidates else ["继续学习", "查看进度"])})
        return common
    if action in ("start", "continue"):
        common.update({"view": "start", "experience": action == "start" and not summary["has_history"],
                       "recommended": metrics["recommended"],
                       "next_options": ["开始讲解", "查看知识地图", "返回学习控制台"]})
        return common
    common.update({"view": "unknown", "next_options": ["$teach 帮助", "$teach", "$teach 继续"]})
    return common


def draft_warning(course):
    if course.get("status") == "draft" or course.get("review_required"):
        return "注意：这是 draft/test 课程，仅用于结构和流程测试，尚不适合作为正式学习材料。"
    return ""


def render_text(result):
    view = result["view"]
    if view == "no_courses":
        return "Teach 学习控制台\n\n暂无已安装的有效课程。请联系课程维护者安装审核后的课程包；我不会临时编造课程。\n\n下一步：$teach 帮助"
    if view in ("choose_course", "invalid_course"):
        lines = ["请选择课程："] + [f"{i}. {item['title']}（{item['version']}，{'有学习记录' if item['has_history'] else '无学习记录'}）" for i, item in enumerate(result["courses"], 1)]
        lines.append("\n回复课程名称或课程 ID 后继续。")
        return "\n".join(lines)
    if view == "courses":
        if not result["courses"]:
            return "已安装课程：暂无。\n\n下一步：$teach 帮助"
        lines = ["已安装课程："]
        for item in result["courses"]:
            warning = "draft/test" if item["status"] == "draft" or item["review_required"] else item["status"]
            lines.append(f"- {item['title']}｜{item['version']}｜{warning}｜{'有学习记录' if item['has_history'] else '无学习记录'}")
        lines.append("\n下一步：选择课程，或输入 $teach 返回控制台。")
        return "\n".join(lines)
    if view == "help":
        return ("Teach 使用帮助\n\n"
                "- $teach：打开学习控制台\n- $teach 开始：开始短体验或新学习\n- $teach 继续：继续上次课程\n"
                "- $teach 进度：查看掌握证据与下一步\n- $teach 课程：查看已安装课程\n- $teach 知识点：查看分组知识地图\n"
                "- $teach 复习：复习到期或薄弱内容\n- $teach 帮助：显示本页\n\n"
                "自然语言也可以，例如“查看学习进度”“这门课有哪些知识点”“复习薄弱部分”。")
    course = result["course"]
    warning = draft_warning(course)
    metrics = result["metrics"]
    if view == "new_home":
        return (f"欢迎来到 Teach 学习控制台\n\n课程：{course['title']}\n{warning}\n\n"
                "1. 开始 5 分钟体验\n2. 查看课程知识地图\n3. 查看学习进度\n4. 使用帮助\n\n"
                "“5 分钟”表示低门槛短体验，不承诺准确计时。")
    if view == "returning_home":
        last = metrics["last_node"]
        last_text = f"{last['title']}（{last['status']}）" if last else "暂无可识别位置"
        recommended = metrics["recommended"]
        rec_text = f"{recommended['title']}（{recommended['reason']}）" if recommended else "暂无"
        return (f"欢迎回来\n\n课程：{course['title']}\n{warning}\n上次位置：{last_text}\n"
                f"掌握证据：verified {metrics['counts']['verified']}，durable {metrics['counts']['durable']}\n"
                f"待复习：{len(metrics['due'])}｜薄弱项：{len(metrics['weak'])}\n推荐下一步：{rec_text}\n\n"
                "下一步：继续学习｜复习｜查看进度｜查看知识地图")
    if view == "progress":
        counts = metrics["counts"]
        last = metrics["last_node"]
        lines = [f"学习进度｜{course['title']}", warning]
        if not course["has_history"]:
            lines.append("暂无学习记录。")
        lines.extend([f"上次节点：{last['title']}（{last['status']}）" if last else "上次节点：无",
                      "掌握证据：" + "｜".join(f"{state} {counts[state]}" for state in STATES),
                      f"待复习：{len(metrics['due'])}｜薄弱项：{len(metrics['weak'])}"])
        if metrics["recommended"]:
            lines.append(f"推荐下一步：{metrics['recommended']['title']}（{metrics['recommended']['reason']}）")
        lines.append("完成或接触不等于掌握；只有独立提取或应用证据才能进入 verified/durable。")
        lines.append("\n下一步：继续学习｜复习｜查看知识地图")
        return "\n".join(item for item in lines if item)
    if view == "knowledge":
        lines = [f"课程知识地图｜{course['title']}", warning,
                 "分组依据：原稿一级标题；若缺少模块字段，不额外编造模块。"]
        for item in result["groups"]:
            lines.append(f"- {item['id']} {item['title']}：{item['node_count']} 个节点，已验证/稳固 {item['verified_or_durable']}")
        if result["selected_group"]:
            lines.append("\n已展开节点：")
            for node in result["selected_group"]["nodes"]:
                lines.append(f"- {node['title']}｜{node['status']}｜前置：{', '.join(node['prerequisites']) or '无'}")
        else:
            lines.append("\n回复一个分组 ID 可展开节点和前置关系；默认不一次列出全部节点。")
        lines.append("下一步：展开分组｜继续学习｜查看进度")
        return "\n".join(item for item in lines if item)
    if view == "review":
        if result["review_kind"] == "none":
            return (f"复习｜{course['title']}\n\n当前没有到期复习或明确薄弱项。不会为了填满列表而编造复习任务。\n\n"
                    "下一步：继续学习｜查看进度")
        label = "到期复习" if result["review_kind"] == "due" else "薄弱项复习"
        items = "\n".join(f"- {item['title']}（{item['status']}）" for item in result["review_candidates"][:5])
        return f"{label}｜{course['title']}\n\n{items}\n\n下一步：开始复习｜查看进度｜继续学习"
    if view == "start":
        item = result["recommended"]
        if not item:
            return f"{course['title']} 当前没有可推荐的下一节点。\n\n下一步：查看进度｜查看知识地图"
        prefix = "先从一个短单元开始体验；不承诺准确 5 分钟。\n" if result["experience"] else ""
        return (f"{prefix}推荐节点：{item['title']}\n选择理由：{item['reason']}\n{warning}\n\n"
                "下一步：开始讲解｜查看知识地图｜返回学习控制台")
    return ("我没有识别这个动作。可以输入 $teach 帮助，或直接说“继续上次课程”“查看学习进度”“复习薄弱部分”。\n\n"
            "下一步：$teach 帮助｜$teach｜$teach 继续")


def main() -> int:
    parser = argparse.ArgumentParser(description="Teach 学习控制台的确定性意图路由与数据汇总")
    parser.add_argument("query", nargs="?", default="", help="例如 $teach、查看学习进度、复习薄弱部分")
    parser.add_argument("--course", help="明确选择课程 ID")
    parser.add_argument("--group", help="知识地图分组 ID")
    parser.add_argument("--format", choices=["json", "text"], default="json")
    parser.add_argument("--courses-root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "references" / "courses")
    parser.add_argument("--state-root", type=Path, default=default_state_root())
    parser.add_argument("--now", help="测试用 ISO 时间；默认当前 UTC 时间")
    args = parser.parse_args()
    now = parse_time(args.now) if args.now else datetime.now(timezone.utc)
    if now is None:
        parser.error("--now 必须是 ISO 时间")
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    action = normalize_action(args.query)
    result = build_result(action, load_courses(args.courses_root, args.state_root), args.course, args.group, now)
    if args.format == "text":
        print(render_text(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
