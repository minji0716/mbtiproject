import streamlit as st
    "ESTJ": {
        "pokemon": "보스로라",
        "emoji": "⛓️🦖",
        "description": "체계적이고 강인한 당신! 단단한 보스로라의 느낌이 있어요."
    },
    "ESFJ": {
        "pokemon": "님피아",
        "emoji": "🎀💕",
        "description": "친절하고 사랑스러운 당신! 따뜻한 매력의 님피아가 딱이에요."
    },
    "ISTP": {
        "pokemon": "루카리오",
        "emoji": "🥋💙",
        "description": "조용하지만 강한 당신! 냉철한 루카리오와 닮았어요."
    },
    "ISFP": {
        "pokemon": "나인테일",
        "emoji": "🦊🔥",
        "description": "예술 감각이 뛰어난 당신! 우아한 나인테일과 잘 어울려요."
    },
    "ESTP": {
        "pokemon": "번치코",
        "emoji": "🥊🔥",
        "description": "에너지 넘치고 도전적인 당신! 뜨거운 열정의 번치코 스타일이에요."
    },
    "ESFP": {
        "pokemon": "푸린",
        "emoji": "🎤💗",
        "description": "분위기 메이커인 당신! 귀엽고 사랑스러운 푸린과 찰떡궁합!"
    }
}

# 제목
st.title("🎮 MBTI 포켓몬 추천기 ✨")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요! 💖")

# MBTI 선택
mbti = st.selectbox(
    "🧩 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

# 버튼
if st.button("🔮 포켓몬 추천받기!"):
    result = pokemon_data[mbti]

    st.balloons()

    st.markdown("---")
    st.subheader(f"🌟 당신에게 어울리는 포켓몬은... {result['pokemon']}! 🌟")

    st.markdown(
        f"""
        ## {result['emoji']}

        ### 💫 추천 포켓몬: **{result['pokemon']}**

        📝 {result['description']}
        """
    )

    st.success("✨ 오늘도 포켓몬처럼 멋진 하루 보내세요! ✨")

# 하단 문구
st.markdown("---")
st.caption("Made with 💖 using Streamlit")
