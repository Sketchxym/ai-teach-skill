#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

STATES = ["unseen", "exposed", "practiced", "verified", "durable"]


def state_root() -> Path:
    explicit = os.environ.get("TEACH_STATE_HOME")
    if explicit:
        return Path(explicit)
    if os.name == "nt" and os.environ.get("LOCALAPPDATA"):
        return Path(os.environ["LOCALAPPDATA"]) / "TeachSkill"
    if os.environ.get("XDG_STATE_HOME"):
        return Path(os.environ["XDG_STATE_HOME"]) / "teach-skill"
    return Path.home() / ".local" / "state" / "teach-skill"


def safe_id(value: str) -> str:
    if not value or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in value):
        raise ValueError("ID 只能包含英文字母、数字、连字符和下划线")
    return value


def load(course: str) -> tuple[Path, dict]:
    path = state_root() / f"{safe_id(course)}.json"
    if path.exists():
        return path, json.loads(path.read_text(encoding="utf-8"))
    return path, {"schema_version": 1, "course_id": course, "nodes": {}}


def main() -> int:
    parser = argparse.ArgumentParser(description="读取或更新 Teach 的本地学习状态")
    sub = parser.add_subparsers(dest="command", required=True)
    show = sub.add_parser("show", help="显示指定课程的学习状态")
    show.add_argument("--course", required=True, help="稳定的课程 ID")
    update = sub.add_parser("update", help="根据可观察到的学习证据更新一个节点")
    update.add_argument("--course", required=True, help="稳定的课程 ID")
    update.add_argument("--node", required=True, help="稳定的知识节点 ID")
    update.add_argument("--status", choices=STATES, required=True, help="证据状态枚举值")
    update.add_argument("--note", default="", help="简短的证据备注，请勿包含敏感信息")
    args = parser.parse_args()
    path, data = load(args.course)
    if args.command == "show":
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0
    node = safe_id(args.node)
    now = datetime.now(timezone.utc).isoformat()
    old = data["nodes"].get(node, {})
    data["nodes"][node] = {
        "status": args.status,
        "updated_at": now,
        "attempts": int(old.get("attempts", 0)) + 1,
        "review_due": old.get("review_due"),
        "note": args.note[:500],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
