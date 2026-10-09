# 2. 在 Transformer 之前：RNN 像一场接力跑

<!-- node_id: 2-transformer-rnn; source_lines: 65-76; review_required: true -->

## 原稿摘录

RNN 处理句子时，会不断更新一个隐藏状态：

\[
h_t=f(x_t,h_{t-1})
\]

第 \(t\) 步的结果依赖第 \(t-1\) 步，因此一句话必须大致按顺序计算。

这带来两个问题。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
