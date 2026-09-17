from os import name

import streamlit as st
# 设置页面
import streamlit as st

st.set_page_config(
    page_title="stream 入门",
     page_icon="🧊",#图标
    layout="wide",#占用区域
    initial_sidebar_state="expanded",#侧边栏
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# 这是一个入门程序!"
    }
)


# 大标题
st.title("streamlit 入门演示")
st.header("streamlit 一级标题")
st.subheader("streamlit 二级标题")


# 段落文字
st.write("布偶猫，又称“仙女猫”，是猫界中体型最大、毛发最华丽的品种之一。它们诞生于20世纪60年代的美国，由育种家安·贝克精心培育而成。布偶猫最引人注目的特征是那双湛蓝如海的眼睛，配合重点色、双色或手套色等丰富花色，宛如戴着一副精致面具。它们拥有丝滑的半长毛，脖颈处如围脖般蓬松，触感柔软似云朵。")
st.write("性格是布偶猫最大的魅力所在——温顺、安静、亲人，痛感耐受度高，被抱起时会像布偶一样全身放松，因此得名。它们喜欢跟随主人从一个房间走到另一个房间，乐于互动，甚至能像小狗一样玩巡回游戏。布偶猫成熟较晚，需3至4年才完全长成，体重可达5至9公斤。")
st.write("养护方面，需每日梳理毛发防止打结，注意控制体重并保持环境清洁。若你渴望一只温柔忠诚、能陪伴左右的“毛绒巨婴”，布偶猫无疑是理想选择。")


# 图片
# st.image("./resources/pexels.jpg")
st.image("resources/pexels.jpg")

# 音频
st.audio("resources/aigei.mp3")

# 视频
st.video("resources/tutorial-video.mp4")

# logo
st.logo("resources/dbf.png")
# 表格
student_date = {
    "姓名" : [ "王林" ,"李慕婉" ,"贝罗" ,"莫里海" ,"是校" ],
    "学号" : ["26001","26002","26003","26004","26005"],
    "语文" : [1,2,3,4,5],
    "数学" : [1,2,3,4,5],
    "英语" : [1,2,3,4,5],
    "总分" : [3,6,9,12,15]
}
st.table(student_date)

# 输入框
#普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为 : {name}")

#密码输入框
password = st.text_input("请输入密码" , type="password")
st.write(f"您输入的密码为 : {password}")

# 单选
gender = st.radio("请输入您的性别" ,["男","女","未知"])
st.write (f"您的性别为: {gender}")