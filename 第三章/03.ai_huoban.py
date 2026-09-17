from os import name
import os
from openai import OpenAI

import streamlit as st
# 设置页面
import streamlit as st

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
system_prompt = "你是一名可爱的AI助理,你的名字叫小甜甜,请你用温柔可爱的的语气回答用户问题"

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages: #{ "role": "user", "content": "..." }
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])


# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY 环境变量名字 , 值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

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
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回结果
    print("AI: " + response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存大模型输入的提示词
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

