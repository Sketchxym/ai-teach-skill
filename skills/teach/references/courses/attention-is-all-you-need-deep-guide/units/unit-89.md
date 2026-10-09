# 参考资料与讲解设计来源

<!-- node_id: unit-89; source_lines: 1049-1065; review_required: true -->

## 原稿摘录

事实、公式与实验数据以原论文和作者资料为准：

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [NeurIPS 2017 正式收录页面](https://papers.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- Jakob Uszkoreit, [Transformer: A Novel Neural Network Architecture for Language Understanding](https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/)

讲解结构参考了几类优秀教程的长处：

- Jay Alammar, [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)：从黑盒到组件、再从单词级向量推进到矩阵计算。
- Harvard NLP, [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)：把论文公式、网络模块、训练循环和实现对应起来。
- [Dive into Deep Learning：Attention 与 Transformer 章节](https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)：先铺垫 Q/K/V 与注意力评分，再进入多头和完整架构。
- TensorFlow, [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer)：沿可运行系统解释数据、Mask、训练和推理。
- Stanford CS224N, [Transformers 课程资料](https://web.stanford.edu/class/cs224n/)：将注意力、训练技巧与后续预训练模型放进课程脉络。

本文没有照搬上述文章，而是综合它们的讲解顺序，重新组织为“问题 → 数学预备 → 单次计算 → 矩阵形状 → 零件 → 整机 → 训练与推理 → 实验与边界”的中文入门路径。

## 教学草稿

待审核：仅使用原稿能够支持的材料，补充学习目标、“是什么、为什么、怎么用”、示例、反例和常见误区。
