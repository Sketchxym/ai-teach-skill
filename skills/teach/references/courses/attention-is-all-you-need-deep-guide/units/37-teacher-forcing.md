# 37. Teacher Forcing 带来的训练—推理差异

<!-- node_id: 37-teacher-forcing; source_lines: 693-698; review_required: true -->

## 原稿摘录

训练时模型看到的历史通常是真实 token；推理时看到的是自己之前生成的 token。如果早期生成错了，错误可能继续影响后续，这种差异常被称为 exposure bias。

它不是 Transformer 独有的问题，而是许多自回归序列模型共同面对的问题。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
