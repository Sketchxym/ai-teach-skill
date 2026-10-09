# 42.2 Label Smoothing

<!-- node_id: 42-2-label-smoothing; source_lines: 789-794; review_required: true -->

## 原稿摘录

普通交叉熵常把正确 token 的目标概率视为 1、其他为 0。Label smoothing 将目标分布稍微摊平。论文使用 \(\epsilon_{ls}=0.1\)。

论文报告它会让 perplexity 变差，因为模型被训练得不那么自信，却能提高准确率和 BLEU。这提醒我们：不同指标衡量的并不是完全相同的东西。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
