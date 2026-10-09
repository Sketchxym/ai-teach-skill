# 12. 单个 Query 的四步计算

<!-- node_id: 12-query; source_lines: 233-250; review_required: true -->

## 原稿摘录

核心公式为：

\[
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

把它从内向外读：

1. \(QK^T\)：每个 Query 和每个 Key 做点积。
2. 除以 \(\sqrt{d_k}\)：控制分数尺度。
3. softmax：把每行分数变成概率式权重。
4. 乘以 \(V\)：对 Value 加权求和。

![Q、K、V 到注意力输出的四步计算](imgs/03-flowchart-qkv-attention.png)

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
