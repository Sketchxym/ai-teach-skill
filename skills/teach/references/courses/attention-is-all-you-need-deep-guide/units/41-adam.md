# 41. Adam 与特殊学习率计划

<!-- node_id: 41-adam; source_lines: 758-782; review_required: true -->

## 原稿摘录

论文使用 Adam：

\[
\beta_1=0.9,\quad\beta_2=0.98,\quad\epsilon=10^{-9}
\]

学习率为：

\[
lrate=d_{model}^{-0.5}\cdot
\min(step^{-0.5},\ step\cdot warmup^{-1.5})
\]

其中 warmup steps 为 4000。

这表示：

- 前 4000 步，学习率线性上升；
- 之后按步数的平方根倒数下降；
- 模型维度越大，整体学习率尺度越低。

Warmup 的直觉是：训练初期参数和优化器动量估计都不稳定，先慢慢提高步长，再进入衰减阶段。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
