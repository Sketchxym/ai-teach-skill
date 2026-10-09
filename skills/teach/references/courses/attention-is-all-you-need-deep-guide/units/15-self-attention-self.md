# 15. Self-Attention 的“Self”是什么意思？

<!-- node_id: 15-self-attention-self; source_lines: 313-326; review_required: true -->

## 原稿摘录

如果 Q、K、V 都来自同一段序列，就是 Self-Attention：这段序列在观察自己。

以输入矩阵 \(X\) 表示整句话：

\[
Q=XW^Q,\quad K=XW^K,\quad V=XW^V
\]

Encoder Self-Attention 中，每个输入位置都能关注全部输入位置。Decoder 的 Masked Self-Attention 也来自同一输出序列，但未来位置会被遮住。

如果 Q 来自 Decoder，而 K、V 来自 Encoder，就不是 Self-Attention，而是 **Cross-Attention（交叉注意力）**。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
