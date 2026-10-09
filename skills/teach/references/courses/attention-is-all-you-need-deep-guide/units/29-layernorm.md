# 29. LayerNorm 在规范什么？

<!-- node_id: 29-layernorm; source_lines: 554-571; review_required: true -->

## 原稿摘录

LayerNorm 对单个 token 表示内部的特征维进行归一化。它不同于依赖批次统计量的 BatchNorm，因此更适合变长序列和自回归模型。

原论文的子层结构是：

\[
LayerNorm(x+Sublayer(x))
\]

也就是先经过子层，做残差相加，再归一化，通常叫 **Post-Norm**。许多后续大模型使用 Pre-Norm：

\[
x+Sublayer(LayerNorm(x))
\]

后者常让深层网络更容易优化，但它不是 2017 年原论文配置。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
