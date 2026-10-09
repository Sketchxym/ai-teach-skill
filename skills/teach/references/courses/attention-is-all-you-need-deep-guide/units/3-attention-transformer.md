# 3. Attention 在 Transformer 之前已经存在

<!-- node_id: 3-attention-transformer; source_lines: 87-96; review_required: true -->

## 原稿摘录

Transformer 并不是注意力机制的发明者。早期神经机器翻译常使用 RNN Encoder–Decoder：Encoder 把输入压缩成表示，Decoder 逐词生成。Bahdanau Attention 等工作让 Decoder 在每一步都能回看 Encoder 的不同位置，从而缓解“整个句子只能塞进一个固定向量”的瓶颈。

但当时的 Attention 通常是 **RNN 的辅助部件**。2017 年论文真正激进的地方是：

> 如果 Attention 已经可以直接在任意位置之间搬运信息，能不能把循环层和卷积层都拿掉？

Transformer 的答案是可以。论文用 Self-Attention 作为序列内部主要的信息交换机制。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
