# 51. “Attention is all you need” 不等于模型只剩 Attention

<!-- node_id: 51-attention-is-all-you-need-attention; source_lines: 959-972; review_required: true -->

## 原稿摘录

完整模型仍然依赖：

- tokenization 与 embedding；
- 位置编码；
- FFN；
- 残差连接；
- LayerNorm；
- Linear + softmax；
- 优化器、学习率、正则化和解码策略。

标题强调的是：序列位置之间的信息交换不再必须依赖循环或卷积。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
