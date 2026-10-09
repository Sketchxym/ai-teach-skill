# 50. GPT 不是原论文 Decoder 的原样复制

<!-- node_id: 50-gpt-decoder; source_lines: 941-956; review_required: true -->

## 原稿摘录

它们共享的核心包括多头注意力、残差、归一化、FFN 和堆叠结构，但现代模型常修改：

- LayerNorm 位置与形式；
- 位置表示，如 RoPE、相对位置偏置；
- 激活函数，如 GELU、SwiGLU；
- 注意力变体，如 multi-query 或 grouped-query attention；
- FFN 宽度、头维度、残差缩放；
- tokenizer、训练目标、数据规模和后训练方式；
- 推理缓存与系统优化。

因此，原论文是共同祖先，不是现代大模型的完整施工图。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
