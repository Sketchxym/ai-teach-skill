# 31. Decoder 每层为什么有三个子层？

<!-- node_id: 31-decoder; source_lines: 592-605; review_required: true -->

## 原稿摘录

一个 Decoder 层包含：

1. **Masked Self-Attention**：读取已经出现的目标 token。
2. **Cross-Attention**：读取 Encoder 的源句表示。
3. **FFN**：逐位置加工。

三者分别回答：

- 我已经生成了什么？
- 原文里哪些位置与当前生成最相关？
- 如何进一步变换当前表示？

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
