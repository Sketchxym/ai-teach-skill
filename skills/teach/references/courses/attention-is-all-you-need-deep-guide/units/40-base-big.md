# 40. Base 与 Big 配置

<!-- node_id: 40-base-big; source_lines: 746-757; review_required: true -->

## 原稿摘录

| 配置 | Base | Big |
|---|---:|---:|
| Encoder 层 | 6 | 6 |
| Decoder 层 | 6 | 6 |
| \(d_{model}\) | 512 | 1024 |
| FFN 维度 | 2048 | 4096 |
| 注意力头 | 8 | 16 |
| Dropout | 0.1 | 0.3（英德 Big） |
| 参数量 | 约 65M | 约 213M |

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
