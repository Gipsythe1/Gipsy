import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="TradeLingo: 3-Month Trading Masterclass",
    page_icon="📈",
    layout="centered"
)

# Initialize Session State for Gamification (Streak, XP, Hearts, Progress)
if "streak" not in st.session_state:
    st.session_state.streak = 3
if "xp" not in st.session_state:
    st.session_state.xp = 85
if "hearts" not in st.session_state:
    st.session_state.hearts = 5
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = []
if "current_view" not in st.session_state:
    st.session_state.current_view = "path" # Options: "path", "lesson"
if "active_lesson" not in st.session_state:
    st.session_state.active_lesson = None

# Custom CSS styling to mimic clean modern UI and gamified status bars
st.markdown("""
    <style>
    .stat-box {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Top Gamification Dashboard Header
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='stat-box'>🔥 Streak: {st.session_state.streak}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='stat-box'>⚡ XP: {st.session_state.xp}</div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='stat-box'>❤️ Hearts: {st.session_state.hearts}/5</div>", unsafe_allow_html=True)
with col4:
    if st.button("🏠 Home"):
        st.session_state.current_view = "path"
        st.rerun()

st.divider()

# Lesson Curriculum Database
curriculum = {
    1: {
        "title": "Month 1: Foundations & Market Mechanics",
        "lessons": [
            {
                "id": 101,
                "title": "Week 1: Market Participants & Asset Classes",
                "content": "Financial markets consist of retail traders, institutions, and central banks. Assets span Stocks, Forex, and Crypto.",
                "question": "Which market participant typically commands the largest institutional liquidity volume?",
                "options": ["Retail Day Traders", "Central Banks & Major Institutions", "Independent Freelancers", "Algorithmic Hobbyists"],
                "answer": "Central Banks & Major Institutions"
            },
            {
                "id": 102,
                "title": "Week 4: Risk Management & The 2% Rule",
                "content": "Capital preservation is paramount. Never risk more than 1% to 2% of your total account balance on a single trade setup.",
                "question": "If your trading account balance is $10,000, what is the maximum risk amount under the 2% rule?",
                "options": ["$50", "$200", "$500", "$1,000"],
                "answer": "$200"
            }
        ]
    },
    2: {
        "title": "Month 2: Technical Analysis & Strategy",
        "lessons": [
            {
                "id": 201,
                "title": "Week 5: Support & Resistance Zones",
                "content": "Support acts as a floor where buying interest overcomes selling pressure. Resistance acts as a ceiling where selling pressure builds.",
                "question": "When price breaks cleanly *above* a major resistance level, what does that level typically turn into?",
                "options": ["A new Support level", "A liquidity trap", "A margin call", "Zero volatility"],
                "answer": "A new Support level"
            }
        ]
    },
    3: {
        "title": "Month 3: Psychology & Live Execution",
        "lessons": [
            {
                "id": 301,
                "title": "Week 9: Managing Trading Psychology",
                "content": "Revenge trading and FOMO (Fear of Missing Out) are psychological traps that wipe out profitable accounts.",
                "question": "What is the best psychological response after taking two consecutive unexpected stop-loss hits?",
                "options": ["Double your position size to recover losses", "Step away, review the trading journal, and clear your head", "Switch to high-leverage crypto futures", "Blame the broker"],
                "answer": "Step away, review the trading journal, and clear your head"
            }
        ]
    }
}

# View 1: Learning Path (Curriculum Tree)
if st.session_state.current_view == "path":
    st.subheader("🗺️ Your 3-Month Trading Path")
    st.write("Complete bite-sized lessons daily to keep your streak alive and unlock advanced strategies.")

    for month_num, month_data in curriculum.items():
        st.markdown(f"### {month_data['title']}")
        for lesson in month_data["lessons"]:
            is_completed = lesson["id"] in st.session_state.completed_lessons
            status_icon = "✅" if is_completed else "🔓"
            
            col_l, col_r = st.columns([4, 1])
            with col_l:
                st.write(f"{status_icon} **{lesson['title']}**")
            with col_r:
                if st.button("Start", key=f"btn_{lesson['id']}"):
                    st.session_state.active_lesson = lesson
                    st.session_state.current_view = "lesson"
                    st.rerun()
        st.write("")

# View 2: Active Bite-Sized Lesson Interface
elif st.session_state.current_view == "lesson":
    lesson = st.session_state.active_lesson
    st.subheader(f"📖 Lesson: {lesson['title']}")
    
    # Concept explanation block
    st.info(lesson["content"])
    
    st.divider()
    st.markdown(f"#### 🧠 Quick Check: {lesson['question']}")
    
    # Interactive Multiple-Choice Selection
    user_choice = st.radio("Select your answer:", lesson["options"], key=f"q_{lesson['id']}")
    
    if st.button("Check Answer"):
        if st.session_state.hearts <= 0:
            st.error("❤️ You are out of hearts! Review previous lessons or wait to recharge.")
        elif user_choice == lesson["answer"]:
            st.success("Correct! 🎉 Great job keeping your discipline sharp.")
            if lesson["id"] not in st.session_state.completed_lessons:
                st.session_state.completed_lessons.append(lesson["id"])
                st.session_state.xp += 15
                st.session_state.streak += 1
            
            if st.button("Continue to Path"):
                st.session_state.current_view = "path"
                st.rerun()
        else:
            st.session_state.hearts -= 1
            st.error(f"Incorrect! ❌ You lost a heart. Hearts remaining: {st.session_state.hearts}")
            if st.session_state.hearts <= 0:
                st.warning("Out of hearts! Take a quick break to reset your mindset.")
