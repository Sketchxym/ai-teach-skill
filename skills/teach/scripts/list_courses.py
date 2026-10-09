#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="列出 Teach 当前可以发现的本地课程")
    parser.add_argument("--courses-root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "references" / "courses",
                        help="课程库目录；默认使用当前 Skill 的 references/courses")
    args = parser.parse_args()
    root = args.courses_root
    found = []
    if root.exists():
        for child in sorted(p for p in root.iterdir() if p.is_dir()):
            manifest = child / "course.yaml"
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
                found.append({
                    "id": data["id"], "title": data["title"], "path": str(child),
                    "status": data.get("status", "unknown"),
                    "review_required": bool(data.get("review_required", False)),
                })
            except (OSError, ValueError, KeyError):
                continue
    print(json.dumps({"courses": found, "count": len(found)}, ensure_ascii=False, indent=2))
    if not found:
        print("暂无已安装的有效课程。请联系课程维护者，把审核通过的课程包放入 references/courses/。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
