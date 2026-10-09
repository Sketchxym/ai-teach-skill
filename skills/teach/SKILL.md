---
name: teach
description: 打开 Teach 学习控制台或使用本地课程进行自适应教学；支持开始、继续、进度、课程、知识点、复习和帮助，并根据前置知识与掌握证据选择下一节点。课程库为空时不得临时编造课程。
---

# Teach

始终在主对话中教学。学习者可以随时打断提问；简洁回答，记录有用的学习信号，再回到当前学习主线。

把 `$teach`、`$teach 开始|继续|进度|课程|知识点|复习|帮助` 及等价自然语言交给学习控制台。在本 Skill 目录运行 `python scripts/learning_console.py "用户表达" --format json`，并按[学习控制台规范](references/learning-console.md)呈现结果。不要依赖宿主专属 slash command。

进入 `开始`或`继续`后：

1. 阅读[教学运行规则](references/teaching-runtime.md)，再读取所选课程的 `course.yaml`、`graph.yaml`，以及当前确实需要的单元和测验文件。
2. 综合目标相关度、前置知识、已有证据和复习时间选择下一节点，不得只按文件顺序推进。
3. 每次完成一个小单元的讲解与测验，只根据实际表现更新状态。
4. 提供简短的继续、复习或切换选项。宿主支持可点击提问组件时优先使用；否则显示编号选项。

课程库为空时明确提示，不要求学习者上传资料，也不临时编造课程。不得把“听过”“自我感觉良好”“完成页面”或“跳过测验”视为掌握。判断证据前阅读[掌握度规则](references/mastery.md)，写入进度前阅读[学习状态](references/learning-state.md)，解释课程包前阅读[课程格式](references/course-format.md)。
