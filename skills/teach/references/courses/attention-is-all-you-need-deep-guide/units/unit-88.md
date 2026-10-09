# 一页速查表

<!-- node_id: unit-88; source_lines: 1028-1048; review_required: true -->

## 原稿摘录

| 部件 | 一句话职责 |
|---|---|
| Tokenizer | 把文本切成模型可处理的单位 |
| Embedding | 把 token 编号变成连续向量 |
| Positional Encoding | 注入顺序与距离信息 |
| Query | 表达当前需要检索什么 |
| Key | 表达每个位置能如何被匹配 |
| Value | 表达匹配后真正取回的内容 |
| Scaled Dot-Product Attention | 匹配、缩放、归一化、加权汇总 |
| Multi-Head Attention | 在多个投影空间并行建模关系 |
| FFN | 对每个位置独立进行非线性加工 |
| Residual | 保留直通信息与梯度路径 |
| LayerNorm | 稳定单个位置内部的特征尺度 |
| Causal Mask | 阻止 Decoder 看到未来 token |
| Cross-Attention | 让 Decoder 从 Encoder 输出中取信息 |
| Linear + Softmax | 把隐藏向量变成词表概率 |

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
