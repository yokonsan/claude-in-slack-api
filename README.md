# claude-in-slack-api

通过 Slack API 来使用 Claude

`.env.template` 重命名为 `.env` 并填入 Slack APP Token 和 Claude Bot ID

## 运行

```bash
pip install -r requirements.txt
pip install sse-starlette
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

## 公众号文章

[Claude｜媲美ChatGPT，如何免费接入到个人服务](https://mp.weixin.qq.com/s?__biz=Mzg4MjkzMzc1Mg==&mid=2247483961&idx=1&sn=c009f4ea28287daeaa4de17278c8228e&chksm=cf4e68aef839e1b8fe49110341e2a557e0b118fee82d490143656a12c7f85bdd4ef6f65ffd16&token=1094126126&lang=zh_CN#rd)
