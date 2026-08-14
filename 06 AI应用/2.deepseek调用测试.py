# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建与ai大模型交互的客户端对象，'DEEPSEEK_API_KEY'环境变量的名字，值是deepseek的api_key值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与ai大模型进行交互（）
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你是谁？你能帮我做什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出大模型返回结果
print(response.choices[0].message.content)

# import os
# from openai import OpenAI
#
# client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "你是谁？你能帮我做什么？"},
#     ],
#     stream=True
# )
#
# # 流式循环读取分片
# for chunk in response:
#     if chunk.choices and chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="")
# print()