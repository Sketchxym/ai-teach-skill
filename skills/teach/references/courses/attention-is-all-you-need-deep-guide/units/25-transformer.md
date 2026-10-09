# 25. 先看整台原始 Transformer

<!-- node_id: 25-transformer; source_lines: 507-514; review_required: true -->

## 原稿摘录

原论文采用 Encoder–Decoder 架构，基础模型两边各堆叠 6 层。

![原始 Transformer 编码器—解码器总体结构](../imgs/02-framework-transformer-architecture.png)

Encoder 把输入加工成上下文表示；Decoder 根据已经生成的目标 token，同时读取 Encoder 结果，预测下一个 token。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
