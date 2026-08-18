import os
import json
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
system_prompt="""
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
        规则:
            1.每次只回1条消息
            2.禁止任何场景或状态描述性文字
            3.匹配用户的语言
            4.回复简短，像微信聊天一样了
            5.有需要的话可以用❤️🌺等emoji表情
            6.用符合伴侣性格的方式对话
            7.回复的内容,要充分体现伴侣的性格特征
        伴侣性格：
            -%s
        你必须严格遵守上述规则来回复用户
"""

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小鑫鑫"

#性格
if "nature_description" not in st.session_state:
    st.session_state.nature_description = "一个温柔体贴的河南小伙"

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

#创建与ai大模型交互的客户端对象，'DEEPSEEK_API_KEY'环境变量的名字，值是deepseek的api_key值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#左侧侧边栏 - with:streamlit的上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    #昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入伴侣的昵称",value=st.session_state.nick_name)
    if nick_name != "":
        st.session_state.nick_name = nick_name
    #性格输入框
    nature_description = st.text_area("性格描述",placeholder="请输入伴侣的性格",value=st.session_state.nature_description)
    if nature_description != "":
        st.session_state.nature_description = nature_description
    #描述输入框


#消息输入框
prompt=st.chat_input("请输入您要问的问题")
if prompt:      #字符串自动转化为布尔值，空为false
    st.chat_message("user").write(prompt)  #st.chat_message与st.chat_input配合使用
    print("--------->调用ai答大模型，，提示词：",prompt)

    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用ai大模型
    # print([
    #         {"role": "system", "content": system_prompt},
    #         *st.session_state.messages
    #     ]
    # )
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name,st.session_state.nature_description)},
            *st.session_state.messages   #会话记忆--->解包
        ],
        stream=True
    )

    #输出大模型返回结果（非流式输出）
    # print("<--------- 大模型返回结果：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回结果(流式循环读取分片)
    response_message=st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response = full_response + content
            response_message.chat_message("assistant").write(full_response)

    #保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

