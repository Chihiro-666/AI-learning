#pip install streamlit
import streamlit as st

#页面
import streamlit as st

st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    layout="wide",  #centered
    #侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#标题
st.title("streamlit 入门程序")
st.header("一级标题")
st.subheader("二级标题")

#段落
st.write("布偶猫又称布拉多尔猫，是人工培育的长毛宠物猫，诞生于美国加州，凭借温顺软糯的性格与仙气满满的外形，被大家称作 “仙女猫”，也是当下人气极高的伴侣宠物。")
st.write("布偶属于大体型猫咪，成年公猫体重可达 8-10 公斤，母猫 6-8 公斤，体态修长骨架结实，浑身覆盖蓬松顺滑的中长毛，毛发柔软如云朵，摸起来酷似玩偶，名字也由此而来。")
st.write("它有着标志性湛蓝通透的大眼睛，脸部带有渐变重点色块，常见花色有海豹色、蓝色、巧克力色、淡紫色，按照斑纹样式又分为双色、重点色、手套色、山猫纹。耳朵大小适中，四肢粗壮有力，蓬松修长的尾巴是重要装饰，走动时优雅舒展。毛发日常轻微掉毛，春秋换毛季脱毛会更明显。")

#图片
st.image("./resource/cat.jpg",width=300)

#音频
#st.auio(./resource/news.mp3)

#视频
# st.video("resource/video.mp4")

#logo
# st.logo("resource/video.jpg")

#分割线
# st.divider()

#表格
#字典
data={
    "name":["王林","张三","李四","王五"],
    "age":[20,22,24,23],
    "chinese":["98","89","78","86"],
}
st.table(data)

#输入框
name=st.text_input("请输入姓名：")
st.write(f"您输入的姓名是：{name}")

#单选按钮
gender=st.radio("请输入您的性别：",["男","女","未知"],index=1)
st.write(f"您的性别为：{gender}")

