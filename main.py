import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="✨ MBTI 포켓몬 추천기 ✨",
    page_icon="🎮",
    layout="centered"
)

# 제목
st.markdown("""
# 🎮 MBTI 포켓몬 추천기 ✨
당신의 MBTI에 어울리는 포켓몬은 누구일까요? 🔍  
귀엽고 멋진 포켓몬을 만나보세요! 💖
""")

# MBTI별 데이터
pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠⚡",
        "desc": "전략적이고 똑똑한 당신! 강력한 전설의 포켓몬 뮤츠와 닮았어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    },
    "INTP": {
        "pokemon": "후딘",
        "emoji": "📚🔮",
        "desc": "호기심 많고 분석적인 당신은 IQ 천재 포켓몬 후딘과 찰떡!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png"
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥👑",
        "desc": "카리스마 넘치는 리더 타입! 리자몽처럼 강렬한 존재감!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "😈🎭",
        "desc": "장난기 많고 창의적인 당신은 팬텀과 완벽한 조합!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"
    },
    "INFJ": {
        "pokemon": "가디안",
        "emoji": "💖🔮",
        "desc": "따뜻하고 신비로운 당신은 가디안처럼 모두를 지켜줘요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png"
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🌸🦊",
        "desc": "감성적이고 순수한 당신! 사랑스러운 이브이와 닮았어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"
    },
    "ENFJ": {
        "pokemon": "루카리오",
        "emoji": "✨🐺",
        "desc": "사람들을 이끄는 열정적인 성격! 루카리오와 잘 어울려요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png"
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡🐭",
        "desc": "밝고 에너지 넘치는 당신은 피카츄 그 자체!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "💧🐢",
        "desc": "책임감 있고 믿음직한 당신은 든든한 거북왕 스타일!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "💝🥚",
        "desc": "상냥하고 배려심 많은 당신! 해피너스처럼 따뜻해요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png"
    },
    "ESTJ": {
        "pokemon": "보스로라",
        "emoji": "🛡️⚙️",
        "desc": "체계적이고 강한 리더십! 보스로라와 찰떡궁합!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png"
    },
    "ESFJ": {
        "pokemon": "푸린",
        "emoji": "🎤💗",
        "desc": "친화력 최고! 모두와 잘 어울리는 푸린 타입!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"
    },
    "ISTP": {
        "pokemon": "핫삼",
        "emoji": "⚔️🔴",
        "desc": "쿨하고 실용적인 당신은 핫삼처럼 멋져요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png"
    },
    "ISFP": {
        "pokemon": "나인테일",
        "emoji": "🦊✨",
        "desc": "예술적 감각이 뛰어난 당신! 우아한 나인테일과 닮았어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png"
    },
    "ESTP": {
        "pokemon": "번치코",
        "emoji": "🔥🥊",
        "desc": "도전 정신 넘치는 당신! 액션파 번치코 스타일!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png"
    },
    "ESFP": {
        "pokemon": "꼬부기",
        "emoji": "🌊😆",
        "desc": "귀엽고 인기 많은 당신은 사랑받는 꼬부기!",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"
    }
}

# MBTI 선택
mbti = st.selectbox(
    "📝 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

# 버튼
if st.button("✨ 포켓몬 추천 받기! ✨"):

    data = pokemon_data[mbti]

    st.balloons()

    st.markdown("---")

    # 포켓몬 이름
    st.markdown(f"""
    ## {data['emoji']} 당신의 포켓몬은 {data['pokemon']}!
    """)

    # 포켓몬 이미지
    st.image(data["image"], width=250)

    # 설명
    st.markdown(f"""
    ### 💬 설명
    {data['desc']}
    """)

    # 랜덤 멘트
    cute_comments = [
        "🌟 오늘도 포켓몬처럼 멋진 하루 보내세요!",
        "🎮 당신은 이미 체육관 관장급 매력 보유자!",
        "💖 포켓몬 세계에서도 인기 만점일 타입!",
        "⚡ 당신의 개성은 전설급!"
    ]

    st.success(random.choice(cute_comments))

# 하단 꾸미기
st.markdown("""
---
🎀 Made with Streamlit & Pokémon Love 💖
""")
