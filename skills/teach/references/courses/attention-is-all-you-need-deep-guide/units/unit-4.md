# 贯穿全文的主线案例

<!-- node_id: unit-4; source_lines: 24-45; review_required: true -->

## 原稿摘录

为了避免每一章都换一个例子，后文会反复回到同一项翻译任务：

```text
源句：I love apples.
目标：我 喜欢 苹果。
```

我们会跟着它走完以下路径：

```text
token → embedding → 位置编码
      → Encoder Self-Attention → Encoder 表示
      → Decoder Masked Self-Attention
      → Cross-Attention → 词表概率 → 逐词输出
```

长句中的代词指代仍会作为“为什么需要长距离关系”的补充例子，但所有核心零件都尽量装回这条主线。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
