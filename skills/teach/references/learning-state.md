# 学习状态

学习进度必须与 Skill 和课程安装目录分离，避免更新课程时覆盖个人状态。`scripts/learner_state.py` 按以下优先级确定状态目录：

1. 已明确设置的 `TEACH_STATE_HOME`；
2. Windows 上的 `%LOCALAPPDATA%\TeachSkill`；
3. POSIX 系统上的 `$XDG_STATE_HOME/teach-skill`；
4. 最后的备用路径 `~/.local/state/teach-skill`。

每门课程保存一个 JSON 文件。每个节点记录 `status`、时间戳、下次复习时间、尝试次数和简短的证据备注。尽量通过脚本读写，不要手工修改：

```text
python scripts/learner_state.py show --course COURSE_ID
python scripts/learner_state.py update --course COURSE_ID --node NODE_ID --status practiced --note "Solved with one hint"
```

不能因为页面已经展示或讲解已经发送，就直接更新掌握状态。证据备注中不要写入个人敏感信息。课程更新时应保留稳定节点 ID；对于改名或拆分的节点，必须先应用审核通过的迁移映射。
