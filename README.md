# claude-in-slack-api

通过 Slack API 来使用 Claude

`.env.template` 重命名为 `.env` 并填入 Slack APP Token 和 Claude Bot ID

## 运行

```bash
pip install -r requirements.txt

python claude.py
```

调用接口文档地址：[http://127.0.0.1:8088/docs](http://127.0.0.1:8088/docs)

## 对话

```curl
curl -X 'POST' \
  'http://127.0.0.1:8088/claude/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "你好啊"
}'
```

## 清除上下文

```curl
curl -X 'POST' \
  'http://127.0.0.1:8088/claude/reset' \
  -H 'accept: application/json' \
  -d ''
```
