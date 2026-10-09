# 三种 Attention 放在一起比较

<!-- node_id: attention; source_lines: 635-644; review_required: true -->

## 原稿摘录

| 类型 | Query 来自哪里？ | Key / Value 来自哪里？ | 能看哪些位置？ | 主要作用 |
|---|---|---|---|---|
| Encoder Self-Attention | 当前 Encoder 层输入 | 同一份 Encoder 层输入 | 全部有效源位置 | 让源句内部交换上下文 |
| Decoder Masked Self-Attention | 当前 Decoder 层输入 | 同一份 Decoder 层输入 | 当前位置及过去位置 | 汇总已生成的目标上下文，同时禁止偷看未来 |
| Encoder–Decoder Cross-Attention | Decoder 中间表示 | Encoder 最终输出 | 全部有效源位置 | 根据当前生成需求，从源句中取信息 |

最容易混淆的是 Cross-Attention：它的 Q 与 K/V 不来自同一序列，所以不叫 Self-Attention。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
