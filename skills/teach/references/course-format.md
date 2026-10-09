# 课程包格式

`references/courses/` 下每个课程目录都是一个独立课程包：

```text
course.yaml
graph.yaml
source.md
source-map.yaml
review-report.md
units/<node-id>.md
assessments/<node-id>.yaml
```

本原型中，以 `.yaml` 结尾的文件使用严格 JSON 语法，同时仍属于合法的 YAML 1.2。`course.yaml` 记录课程标识、版本、原稿哈希、组织策略、建议顺序，以及 `status` 和 `intended_use`；`graph.yaml` 是知识节点和依赖边的权威清单；单元文件包含来源信息与教学内容；测验文件把低压力练习和独立提取/迁移测验分开；`source-map.yaml` 负责把生成文件映射回原稿标题与行号范围。

`review_required: true` 是必须处理的审核警告：该内容仍是草稿，不能当成已由原稿充分支持的正式教学内容。不得把占位答案作为权威答案展示。`source.md` 是未经修改的 UTF-8 输入，也是所有来源追踪的基准。

当前构建器生成的课程必须保持 `status: draft` 和 `intended_use: structure_and_flow_testing`。Teach 可以用它测试课程发现、节点路由和交互流程，但应向学习者明确说明它不是正式课程。
