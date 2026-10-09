# 第十二部分：用伪代码把公式落到实现

<!-- node_id: unit-74; source_lines: 881-918; review_required: true -->

## 原稿摘录

下面是接近 PyTorch 写法的核心逻辑。它不是完整可训练模型，但能把公式与代码一一对应：

```python
def scaled_dot_product_attention(q, k, v, mask=None):
    # q, k, v: [batch, heads, seq_len, head_dim]
    scores = q @ k.transpose(-2, -1)
    scores = scores / sqrt(q.size(-1))

    if mask is not None:
        scores = scores.masked_fill(mask == 0, -inf)

    weights = softmax(scores, dim=-1)
    output = weights @ v
    return output, weights
```

多头注意力的外层过程是：

```python
q = split_heads(x @ Wq)
k = split_heads(x @ Wk)
v = split_heads(x @ Wv)

heads, weights = scaled_dot_product_attention(q, k, v, mask)
merged = concat_heads(heads)
output = merged @ Wo
```

请注意三点：

1. `softmax(dim=-1)` 是沿 Key 位置归一化。
2. `mask` 必须能广播到分数形状 `[B, h, n_query, n_key]`。
3. 实际高性能框架可能融合多个操作，不一定真的按这些中间变量逐行执行，但数学等价。

---

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
