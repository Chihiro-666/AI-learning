import os
import json
from datetime import datetime
from openai import OpenAI
import streamlit as st

#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    #布局
    layout="wide",
    #侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#保存会话的函数
def save_session():
    if st.session_state.session_id != "":
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature_description": st.session_state.nature_description,
            "session_id": st.session_state.session_id,
            "messages": st.session_state.messages
        }
        # 创建文件夹
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.session_id}.json", "w",encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识的函数
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

#加载所有会话列表信息
def load_sessions():
    session_list=[]
    #加载sessions目录下的文件
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                session_list.append(file[:-5])
    # 倒序 排序
    session_list.sort(reverse=True)
    return session_list

#加载指定的会话数据的函数
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            #读取会话数据
            with open(f"sessions/{session_name}.json", "r",encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature_description = session_data["nature_description"]
                st.session_state.session_id = session_name
    except Exception:
        st.error("加载会话失败！")

#删除会话信息的函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            #如果删除的是当前会话，则重新生成一个新的会话标识
            if session_name == st.session_state.session_id:
                st.session_state.messages = []
                st.session_state.session_id = generate_session_id()
                save_session()
    except Exception:
        st.error("删除会话失败！")


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

#会话标识 - 时间戳
if "session_id" not in st.session_state:
    st.session_state.session_id = generate_session_id()


#展示聊天信息
st.text("当前会话：%s" % st.session_state.session_id)
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

#创建与ai大模型交互的客户端对象，'DEEPSEEK_API_KEY'环境变量的名字，值是deepseek的api_key值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")


#左侧侧边栏 - with:streamlit的上下文管理器
with (st.sidebar):
    #AI控制面板
    st.subheader("AI控制面板")

    #新建会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        #保存当前会话信息
        save_session()

        #创建新会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.session_id = generate_session_id()
            save_session()
            st.rerun ()  #重新运行页面

    #会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            #加载会话信息
            #三元条件运算符：条件表达式，真值表达式，假值表达式。语法：条件表达式 if 条件 else 条件表达式
            if st.button(session, width="stretch", icon="📂", key=f"load_{session}",type = "primary" if session == st.session_state.session_id else "secondary"):
                load_session(session)
                st.rerun ()
        with col2:
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                if os.path.exists(f"sessions/{session}.json"):
                    delete_session(session)
                    st.rerun ()

    #分割线
    st.divider()

    #伴侣信息
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

    #保存会话信息
    save_session()