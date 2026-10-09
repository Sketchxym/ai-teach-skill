# 8. Softmax：把任意分数变成一组权重

<!-- node_id: 8-softmax; source_lines: 171-186; review_required: true -->

## 原稿摘录

若原始分数为 \([s_1,s_2,s_3]\)，softmax 定义为：

\[
\operatorname{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
\]

结果具有三个性质：

- 每个值都大于 0；
- 所有值加起来等于 1；
- 较大的分数会获得更大的权重。

因此 softmax 可以把“匹配分数”转换成“每个来源应该贡献多少”。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
