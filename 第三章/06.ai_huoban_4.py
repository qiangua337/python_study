from os import name
import os

from numpy.version import full_version
from openai import OpenAI

import streamlit as st
# 设置页面
import streamlit as st
from openai.resources.skills import content

st.set_page_config(
    page_title="AI智能伴侣",
     page_icon="🤖",#图标
    layout="wide",#占用区域
    initial_sidebar_state="expanded",#侧边栏
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

# logo
st.logo("resources/logo2.png")

# 系统提示词
system_prompt =  """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🥰等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容，要充分体现伴侣的性格特征
        
        伴侣性格：
        - %s
        
        你必须严格遵守上述规则来回复用户。
    """

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "小甜甜"

# 性格
if 'nature' not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"


# 展示聊天信息
for message in st.session_state.messages: #{ "role": "user", "content": "..." }
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])


# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY 环境变量名字 , 值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# # 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("昵称")

# 左侧侧边栏 - whit:streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    nick_name = st.text_input("昵称" , placeholder="请输入伴侣昵称" , value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格" , placeholder="请输入伴侣性格" , value=st.session_state.nature  )
    if nature:
        st.session_state.nature = nature


# 聊天输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用ai大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
    )

    # # 输出大模型返回结果(非流式输出)
    # print("AI: " + response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

     # 流式输出
    response_message = st.empty() #创造一个空容器

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

     # 保存大模型输入的提示词
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    