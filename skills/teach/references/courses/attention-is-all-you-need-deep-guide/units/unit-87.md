# 第十五部分：把知识结构压缩成一棵树

<!-- node_id: unit-87; source_lines: 1006-1027; review_required: true -->

## 原稿摘录

读到这里，可以把全文压缩为四层依赖关系：

```text
任务层：序列到序列、理解输入、生成输出
  └─ 架构层：Encoder、Decoder、Linear + Softmax
       └─ 模块层：Self-Attention、Cross-Attention、FFN、残差、LayerNorm
            └─ 运算层：Embedding、位置编码、Q/K/V、点积、缩放、softmax、加权和、Mask
```

运算层回答“一个模块如何计算”；模块层回答“一层网络如何变换信息”；架构层回答“输入如何变成输出”；任务层回答“整台模型为什么存在”。

如果某个概念忘了，不要孤立背诵，而要先问它属于哪一层、为上一层解决了什么问题。例如：

- 位置编码属于运算层，为 Self-Attention 补充顺序；
- Causal Mask 属于运算层，为 Decoder 的自回归约束服务；
- Cross-Attention 属于模块层，为 Decoder 读取 Encoder memory 服务；
- Beam Search 不属于 Transformer 层结构，它是推理解码策略。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
