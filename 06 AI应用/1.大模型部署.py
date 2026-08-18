# 本地部署Olloma

# 官方开放API 应用程序编程接口
# ip地址，127.0.0.1本机，本地环回地址
# 域名localhost,便于记忆
# 端口号0-65535，每个程序

# 云服务平台
#apifox测试

curl:Json格式：一种前端对象表示方法，键值对方式value:key ；所有key用双引号，值：对象、数字、字符串、布尔值、列表
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d '{
        "model": "deepseek-v4-pro",#模型
        #发送的信息
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"}
        ],
        "thinking": {"type": "enabled"},
        "reasoning_effort": "high",
        "stream": false #是否流失
      }'

#会话记忆：消息滚雪球