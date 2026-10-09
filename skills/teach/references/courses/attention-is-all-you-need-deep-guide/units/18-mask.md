# 18. Mask 实际加在哪里？

<!-- node_id: 18-mask; source_lines: 382-406; review_required: true -->

## 原稿摘录

Mask 通常在 softmax 前加入分数矩阵：

\[
S=\frac{QK^T}{\sqrt{d_k}}+M
\]

允许关注的位置，\(M=0\)；禁止关注的位置，\(M=-\infty\)。于是：

\[
\operatorname{softmax}(-\infty)=0
\]

常见 Mask 有两种：

- **Padding Mask**：不让模型关注补齐长度用的空 token。
- **Causal / Look-ahead Mask**：不让 Decoder 看到未来 token。

前者主要处理不同长度的批次，后者保证自回归生成不作弊。

> **装回整机 ③**：现在已经造出单头 Self-Attention。它接收整句矩阵，生成同样长度的新表示；每个位置都按照自己的 Query，从全句 Key/Value 中取回信息。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
