import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="wide"
)

# CSS 꾸미기
st.markdown("""
<style>
.main {
    background-color: #fffaf5;
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #ff66a3;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #666;
}

.pokemon-card {
    background-color: white;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}

.result-title {
    color: #7c4dff;
    font-size: 35px;
    font-weight: bold;
}

.tag {
    display: inline-block;
    background-color: #ffe066;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# MBTI 데이터
pokemon_data = {
    "INFP": {
        "pokemon": "이상해씨 🌱",
        "emoji": "💚✨",
        "desc": "조용하고 따뜻한 마음을 가진 당신! 이상해씨처럼 편안한 매력이 있어요.",
        "tags": ["#감성", "#따뜻함", "#힐링"]
    },

    "INTJ": {
        "pokemon": "뮤츠 🧠",
        "emoji": "⚡👑",
        "desc": "전략적이고 카리스마 넘치는 당신! 강력한 뮤츠 스타일!",
        "tags": ["#천재", "#카리스마", "#분석왕"]
    },

    "ENFP": {
        "pokemon": "피카츄 ⚡",
        "emoji": "💛🎉",
        "desc": "에너지 넘치는 분위기 메이커! 모두에게 사랑받는 피카츄와 찰떡!",
        "tags": ["#활발", "#친화력", "#긍정"]
    },

    "ISTP": {
        "pokemon": "루카리오 🥋",
        "emoji": "💙🔥",
        "desc": "조용하지만 강한 당신! 루카리오 같은 멋짐이 있어요.",
        "tags": ["#쿨함", "#집중력", "#강인함"]
    },

    "ESFP": {
        "pokemon": "푸린 🎤",
        "emoji": "💖🎶",
        "desc": "사람들을 웃게 만드는 당신! 귀여운 푸린과 너무 잘 어울려요.",
        "tags": ["#인싸", "#귀여움", "#행복"]
    }
}

# 제목
st.markdown('<p class="title">🎮 MBTI 포켓몬 추천기 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">당신의 MBTI에 어울리는 포켓몬을 찾아보세요! 💖</p>', unsafe_allow_html=True)

st.write("")

# MBTI 선택
mbti = st.selectbox(
    "🧩 MBTI를 선택해주세요!",
    list(pokemon_data.keys())
)

# 추천 버튼
if st.button("🔮 추천받기!"):

    result = pokemon_data[mbti]

    st.balloons()

    st.markdown("---")

    st.markdown(f"""
    <div class="pokemon-card">

    <div class="result-title">
    {mbti}에게 어울리는 포켓몬은?!
    </div>

    <h1>{result['pokemon']}</h1>

    <h2>{result['emoji']}</h2>

    <p style="font-size:22px;">
    {result['desc']}
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 태그 출력
    for tag in result["tags"]:
        st.markdown(f'<span class="tag">{tag}</span>', unsafe_allow_html=True)

    st.write("")
    st.success("✨ 당신만의 포켓몬 매력을 발견했어요! ✨")

# 사이드바
st.sidebar.title("🌈 오늘의 기분")
mood = st.sidebar.radio(
    "지금 기분은 어떤가요?",
    ["😆 신나요!", "😊 평범해요", "😴 피곤해요", "🔥 열정 폭발!"]
)

st.sidebar.write("💡 MBTI와 포켓몬의 조합을 재미로 즐겨보세요!")

# 하단 문구
st.markdown("---")
st.caption("Made with 💖 using Streamlit")
