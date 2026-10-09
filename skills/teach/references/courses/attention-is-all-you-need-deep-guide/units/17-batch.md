# 17. 带 batch 和多头时，形状如何变化？

<!-- node_id: 17-batch; source_lines: 357-381; review_required: true -->

## 原稿摘录

设：

- batch size：\(B\)
- 序列长度：\(n\)
- 模型维度：\(d_{model}\)
- 头数：\(h\)
- 每头维度：\(d_k=d_{model}/h\)

常见形状是：

| 张量 | 形状 |
|---|---|
| 输入 \(X\) | \([B,n,d_{model}]\) |
| 切分后的 Q/K/V | \([B,h,n,d_k]\) |
| 注意力分数 \(QK^T\) | \([B,h,n,n]\) |
| 每头输出 | \([B,h,n,d_k]\) |
| 拼接后 | \([B,n,h\cdot d_k]\) |
| 输出投影后 | \([B,n,d_{model}]\) |

这张表也解释了长序列为何昂贵：中间分数张量含有 \(B\times h\times n\times n\) 个元素。

![多头注意力中的张量形状变化](../imgs/10-framework-tensor-shapes.png)

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
