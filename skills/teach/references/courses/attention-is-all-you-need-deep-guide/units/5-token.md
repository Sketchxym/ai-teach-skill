# 5. Token：模型处理的基本单位

<!-- node_id: 5-token; source_lines: 119-134; review_required: true -->

## 原稿摘录

模型不会直接读取“句子”。文本先经过 tokenizer，被切成 token。token 可能是一个字、一个词、一个词的一部分，或标点符号。

原论文在英德翻译中使用 byte-pair encoding 一类子词方法，源语言与目标语言共享约 37,000 个 token 的词表；英法任务使用约 32,000 个 word-piece 词表。

初学时可以把 token 暂时理解成“词”，但要知道真实模型经常按子词切分。

在主线案例中，可以先把源句简化成：

```text
[I] [love] [apples] [.]
```

真实 tokenizer 可能采用不同切分，但进入 Transformer 的始终是一串 token 编号。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
