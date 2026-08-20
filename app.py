import streamlit as st
import pandas as pd
import numpy as np
from curriculum import lessons_db

# Page Configuration
st.set_page_config(
    page_title="TradeX - 3-Month Trading Academy",
    page_icon="📈",
    layout="wide"
)

# Initialize Session State
if "xp" not in st.session_state:
    st.session_state.xp = 150
if "hearts" not in st.session_state:
    st.session_state.hearts = 5
if "streak" not in st.session_state:
    st.session_state.streak = 3
if "active_lesson" not in st.session_state:
    st.session_state.active_lesson = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #131722;
        color: #d1d4dc;
    }
    .metric-card {
        background-color: #1e222d;
        border: 1px solid #2a2e39;
        padding: 20px;
        border-radius: 10px;
    }
    .duo-stats {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #1e222d;
        padding: 12px 20px;
        border-radius: 12px;
        border: 1px solid #2a2e39;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .quiz-box {
        background-color: #1e222d;
        border: 1px solid #2a2e39;
        padding: 25px;
        border-radius: 16px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## TRADE<span style='color: #2962ff;'>X</span>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (3-Month Roadmap)", "Global Scoreboard", "Markets", "Paper Trading"])

if page == "Dashboard":
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>WELCOME BACK</p>", unsafe_allow_html=True)
    st.title("Trading Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Portfolio Value</p><h2 style="margin: 0; color: #ffffff;">$10,000.00</h2><span style="color: #089981; font-weight: bold;">+2.45%</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Today\'s Profit</p><h2 style="margin: 0; color: #ffffff;">$245.60</h2><span style="color: #089981; font-weight: bold;">+2.45%</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Available Cash</p><h2 style="margin: 0; color: #ffffff;">$8,750.00</h2><span style="color: #848e9c;">Ready to trade</span></div>', unsafe_allow_html=True)

    st.write("")
    chart_col, watch_col = st.columns([3, 1])
    with chart_col:
        st.markdown("### BTC / USD")
        st.markdown("## $68,420.50")
        chart_data = pd.DataFrame(np.random.randn(50, 1).cumsum() + 68420, columns=["Price"])
        st.line_chart(chart_data, color="#2962ff", height=350)
    with watch_col:
        st.markdown("### Watchlist")
        for asset, price in {"BTC": "$68,420", "ETH": "$3,420", "AAPL": "$227.10", "TSLA": "$341.20"}.items():
            st.markdown(f'<div style="background: #1e222d; padding: 12px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between;"><b>{asset}</b><span style="color: #848e9c;">{price}</span></div>', unsafe_allow_html=True)

elif page == "Trading Academy (3-Month Roadmap)":
    st.markdown(f"""
        <div class="duo-stats">
            <span>🔥 Streak: {st.session_state.streak} Days</span>
            <span>⚡ XP: {st.session_state.xp}</span>
            <span>❤️ Hearts: {'❤️' * st.session_state.hearts}</span>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Curriculum")
    
    cols = st.columns(3)
    for i, (lesson_name, lesson_data) in enumerate(lessons_db.items()):
        col = cols[i % 3]
        if col.button(lesson_name, key=f"btn_{i}"):
            st.session_state.active_lesson = lesson_name
            st.session_state.question_index = 0
            st.rerun()

    if st.session_state.active_lesson:
        lesson = lessons_db[st.session_state.active_lesson]
        st.markdown(f"## {st.session_state.active_lesson}")
        st.info(f"**Concept:** {lesson['concept']}")
        
        q_idx = st.session_state.question_index
        if q_idx < len(lesson['questions']):
            q = lesson['questions'][q_idx]
            st.markdown(f'<div class="quiz-box"><h4>{q["question"]}</h4>', unsafe_allow_html=True)
            
            choice = st.radio("Select an answer:", q['options'], key=f"q_{q_idx}")
            if st.button("Submit Answer"):
                if choice == q['answer']:
                    st.success("Correct!")
                    st.session_state.xp += 10
                else:
                    st.error(f"Wrong. The correct answer was: {q['answer']}")
                    st.session_state.hearts -= 1
                
                st.session_state.question_index += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.success("Lesson Complete!")
            st.session_state.completed_lessons.add(st.session_state.active_lesson)
            if st.button("Return to Roadmap"):
                st.session_state.active_lesson = None
                st.rerun()

elif page == "Global Scoreboard":
    st.title("Global Scoreboard")
    df = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "Trader": ["AlphaTrader", "MarketWizard", "CryptoKing", "RiskManager", "You"],
        "XP": [5400, 5200, 4800, 4500, st.session_state.xp],
        "Win Rate": ["82%", "79%", "75%", "72%", "68%"]
    })
    st.table(df)

elif page == "Markets":
    st.title("Market Overview")
    st.write("Real-time market data integration would appear here.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.write("Practice your skills with $10,000 of virtual capital.")
    
    ticker = st.text_input("Enter Ticker", "BTC")
    amount = st.number_input("Amount", 100, 10000)
    if st.button("Execute Trade"):
        st.write(f"Simulated order placed for {amount} of {ticker}")
                                                   
