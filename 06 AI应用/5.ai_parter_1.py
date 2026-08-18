import os
from openai import OpenAI
import streamlit as st

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    #布局
    layout="wide",
    #侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

#logo
st.logo("resource/logo.png")

#系统提示词
system_prompt="You are a helpful assistant"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

#创建与ai大模型交互的客户端对象，'DEEPSEEK_API_KEY'环境变量的名字，值是deepseek的api_key值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#消息输入框
prompt=st.chat_input("请输入您要问的问题")
if prompt:  #字符串自动转化为布尔值，空为false
    st.chat_message("user").write(prompt)  #st.chat_message与st.chat_input配合使用
    print("--------->调用ai答大模型，，提示词：",prompt)

    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用ai大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    #输出大模型返回结果
    print("<--------- 大模型返回结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)

    #保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

