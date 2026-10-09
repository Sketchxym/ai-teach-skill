# 34. 最后的 Linear + Softmax 如何变成词？

<!-- node_id: 34-linear-softmax; source_lines: 645-662; review_required: true -->

## 原稿摘录

Decoder 顶层输出仍是 \(d_{model}\) 维向量。一个线性层把它映射到词表大小：

\[
logits=hW+b
\]

若目标词表有 32,000 个 token，logits 就有 32,000 个分数。softmax 把它们变成概率分布，再由贪心选择、采样或 beam search 等策略选出 token。

原论文在 embedding 和 softmax 前的线性变换之间共享权重矩阵，以减少参数并利用输入输出表示之间的联系。

在主线案例中，Decoder 从 `<BOS>` 开始预测“我”；生成“我”后再预测“喜欢”；同时每一步通过 Cross-Attention 读取 `I / love / apples` 的 Encoder 表示。

> **装回整机 ⑦**：Decoder 层 = 带因果遮罩的目标端 Self-Attention + 读取源句的 Cross-Attention + FFN。三者的 Q/K/V 来源不同，正是上表要牢牢记住的结构。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
