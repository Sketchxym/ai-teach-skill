# 发布检查记录

版本：`v0.1.0-alpha`

## 自动检查

- 项目 smoke tests：5 项通过；
- Teach Skill 结构校验：通过；
- Course Builder Skill 结构校验：通过（仅用于源项目质量检查，不随公开仓库发布）；
- Transformer 课程校验：0 个结构错误，179 个预期人工审核警告；
- Python 脚本语法检查：通过；
- Codex 与 WorkBuddy ZIP：均包含 Skill、课程关键文件、89 个单元、89 份测验和 12 张图片。

## 敏感信息检查范围

发布前检查所有受 Git 跟踪候选文件的文件名和文本内容，搜索常见 Token、Cookie、Authorization、私钥头、密码字段、本机用户路径及学习状态文件；同时检查 ZIP 条目清单。未发现凭证、私钥、Cookie、用户学习状态或临时缓存。

二进制 PNG 仅作为课程配图纳入。两个 ZIP 是从同一发布内容重新生成的安装产物。
