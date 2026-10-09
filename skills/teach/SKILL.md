---
name: teach
description: 使用已安装的本地课程进行自适应教学；根据学习目标、前置知识、掌握证据和复习需求选择下一知识节点。适用于开始或继续学习课程；课程库为空时不得临时编造课程。
---

# Teach

始终在主对话中教学。学习者可以随时打断提问；简洁回答，记录有用的学习信号，再回到当前学习主线。

首次进入时，在本 Skill 目录运行 `python scripts/list_courses.py`。如果没有已安装的有效课程，请直接说明，并告知需要由课程维护者把审核通过的课程包放入 `references/courses/`；不要要求学习者上传资料，也不要临时生成课程内容。

发现课程后：

1. 确认学习者目标，并用 `python scripts/learner_state.py show --course <id>` 查看历史状态。
2. 阅读[教学运行规则](references/teaching-runtime.md)，再读取所选课程的 `course.yaml`、`graph.yaml`，以及当前确实需要的单元和测验文件。
3. 综合目标相关度、前置知识、已有证据和复习时间选择下一节点，不得只按文件顺序推进。
4. 每次完成一个小单元的讲解与测验，只根据实际表现更新状态。
5. 提供继续、复习或切换节点的选择。宿主支持可点击提问组件时优先使用；否则显示编号选项。

不得把“听过”“自我感觉良好”“完成页面”或“跳过测验”视为掌握。判断证据前阅读[掌握度规则](references/mastery.md)，写入进度前阅读[学习状态](references/learning-state.md)，解释课程包前阅读[课程格式](references/course-format.md)。课程替换、合并或 ID 迁移应使用独立的 `course-builder` Skill 及其维护说明。
