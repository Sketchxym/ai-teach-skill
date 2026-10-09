# 22. Self-Attention 天生像在处理集合

<!-- node_id: 22-self-attention; source_lines: 459-464; review_required: true -->

## 原稿摘录

假设同时打乱输入 token 及其 Q/K/V 的行，注意力会跟着打乱，却不会凭空知道原来的先后顺序。

因此，仅有 Self-Attention 的模型会更像看到“一袋词”。语言中的“我打你”和“你打我”显然不同，必须显式注入位置信息。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
