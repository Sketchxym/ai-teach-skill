# AI Teach Skill

> **公开 Alpha 测试预览（v0.1.0-alpha）**
>
> 当前内置课程仅用于验证 Skill 的目录结构、课程发现、教学状态和交互流程。课程尚未完成语义整理与人工审核，**不适合当作正式学习材料发布或使用**。

AI Teach Skill 是一个本地运行的通用教学框架。它在主对话中带领学习者学习已安装课程，根据学习目标、前置知识、掌握证据和复习需求选择下一知识节点，而不是机械地按章节播放内容。

本仓库只发布面向学习者的 Teach Skill、一个 Transformer 测试课程，以及 Codex 和 WorkBuddy 的测试安装包。课程构建工具不包含在公开仓库中。

## 当前内置测试课程

课程：**真正从零读懂《Attention Is All You Need》**

当前状态：

- 版本为 `0.1.0-draft`；
- 由 Markdown 标题机械拆分为 89 个节点；
- `strategy` 为 `reorganize`，尚未建立真实前置依赖；
- 所有节点、教学草稿和测验均保留 `review_required`；
- 测验仍是占位模板；
- 原稿引用的 12 张配图已经随课程打包；
- 仅适合测试课程发现、节点读取、状态变化和主对话教学流程。

## Codex 安装

仓库发布后，可把下面的 `OWNER` 替换为仓库所有者：

```bash
npx skills add OWNER/ai-teach-skill --skill teach
```

也可以从 GitHub Releases 下载 `teach-codex.zip`，解压后按 Codex 的本地 Skill 安装方式放置 `teach` 目录。

仓库中的可发现入口位于：

```text
skills/teach/SKILL.md
```

其稳定 Skill 名称为 `teach`。

## WorkBuddy 安装

从 GitHub Releases 下载 `teach-workbuddy.zip`，通过 WorkBuddy 的 Skill 导入界面安装。该包使用双语 frontmatter，并与 Codex 包共享同一份教学内核和课程内容。

## 使用示例

安装后可以尝试：

- “教我已安装的 Transformer 测试课程。”
- “从注意力机制开始讲，我不熟悉线性代数。”
- “继续上次的学习。”
- “先跳过测验，继续下一部分。”

跳过测验不会把节点标记为 `verified` 或 `durable`。只有可观察到的独立提取、应用或迁移表现才能形成掌握证据。

## 学习状态存放位置

学习状态不会写入 Skill 或课程安装目录，因此更新 Skill 时不会覆盖个人进度。状态目录按以下顺序确定：

1. 环境变量 `TEACH_STATE_HOME`；
2. Windows：`%LOCALAPPDATA%\TeachSkill`；
3. POSIX：`$XDG_STATE_HOME/teach-skill`；
4. 备用路径：`~/.local/state/teach-skill`。

请勿把包含个人学习记录的状态文件提交到公开仓库。

## 更新

从 Releases 下载新版本并重新安装对应平台包。课程和 Skill 更新不会主动删除独立状态目录，但 Alpha 期间节点 ID 仍可能变化；重大迁移会在 Release notes 中说明。

## 反馈

请通过本仓库的 GitHub Issues 报告：

- 安装或课程发现失败；
- Codex 与 WorkBuddy 的兼容性差异；
- 节点路由、状态更新或中断恢复问题；
- 测试课程中明显的结构或来源映射问题。

请不要在 Issue 中提交 Token、Cookie、私钥、个人学习状态或其他敏感信息。

## 许可证

本仓库当前未声明任何许可证。仓库公开可见不表示授予复制、修改、分发或再许可权。后续许可证决定会单独公告。
