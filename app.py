import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TradeX - Duolingo Style Academy",
    page_icon="📈",
    layout="wide"
)

# Initialize Session State for Gamification (XP, Hearts, Streak)
if "xp" not in st.session_state:
    st.session_state.xp = 150
if "hearts" not in st.session_state:
    st.session_state.hearts = 5
if "streak" not in st.session_state:
    st.session_state.streak = 3
if "active_lesson" not in st.session_state:
    st.session_state.active_lesson = None

# Custom Styling for TradeX Dark Mode + Duolingo-inspired UI Elements
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
        gap: 20px;
        background: #1e222d;
        padding: 10px 20px;
        border-radius: 12px;
        border: 1px solid #2a2e39;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .lesson-node {
        background-color: #1e222d;
        border: 2px solid #2962ff;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        cursor: pointer;
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
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (Duolingo Mode)", "Markets", "Paper Trading"])

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

elif page == "Trading Academy (Duolingo Mode)":
    # Gamification Stats Bar
    st.markdown(f"""
        <div class="duo-stats">
            <span>🔥 Streak: {st.session_state.streak} Days</span>
            <span>⚡ XP: {st.session_state.xp}</span>
            <span>❤️ Hearts: {'❤️' * st.session_state.hearts}</span>
        </div>
    """, unsafe_allow_html=True)

    # Sample Duolingo-style bite-sized lesson database
    lessons_db = {
        "Day 1: What is a Market Maker?": {
            "concept": "Market makers provide liquidity by always being ready to buy or sell at publicly quoted prices.",
            "question": "What is the primary role of a Market Maker?",
            "options": ["To crash the price", "To provide liquidity and facilitate trades", "To charge high trading taxes", "To print money"],
            "answer": "To provide liquidity and facilitate trades"
        },
        "Day 2: Support & Resistance": {
            "concept": "Support is a price floor where buying interest is strong, and resistance is a ceiling where selling pressure takes over.",
            "question": "When price hits a 'Resistance' level, what usually happens?",
            "options": ["Sellers step in and push price down", "Buyers panic and buy everything", "The exchange shuts down", "Nothing changes"],
            "answer": "Sellers step in and push price down"
        },
        "Day 3: The Hammer Candlestick": {
            "concept": "A hammer has a small body and a long lower wick, indicating that sellers tried to push prices down, but buyers rejected it.",
            "question": "What does a long lower wick on a Hammer candle tell you?",
            "options": ["Extreme selling panic", "Price rejection and buyer defense", "Market closure", "Zero volume"],
            "answer": "Price rejection and buyer defense"
        }
    }

    if st.session_state.active_lesson is None:
        st.title("🎯 Choose Your Bite-Sized Mission")
        st.write("Complete quick interactive lessons to earn XP and protect your streak!")
        
        for lesson_title, data in lessons_db.items():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"### {lesson_title}")
                st.write(data["concept"][:80] + "...")
            with col2:
                if st.button("Start Lesson 🚀", key=lesson_title):
                    st.session_state.active_lesson = lesson_title
                    st.rerun()
            st.markdown("---")
            
    else:
        # Active Lesson Interactive Duolingo Quiz Loop
        lesson_key = st.session_state.active_lesson
        current_lesson = lessons_db[lesson_key]
        
        if st.button("⬅️ Back to Map"):
            st.session_state.active_lesson = None
            st.rerun()
            
        st.title(f"📖 Lesson: {lesson_key}")
        
        st.markdown(f"""
        <div class="quiz-box">
            <h4 style="color: #2962ff;">💡 Quick Concept Breakdown</h4>
            <p>{current_lesson['concept']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🧩 Quick Challenge")
        user_choice = st.radio(current_lesson["question"], current_lesson["options"], key="quiz_radio")
        
        if st.button("Check Answer ✅"):
            if user_choice == current_lesson["answer"]:
                st.success("🎉 Correct! Great job! (+15 XP)")
                st.session_state.xp += 15
                if st.button("Continue ➡️"):
                    st.session_state.active_lesson = None
                    st.rerun()
            else:
                st.error("❌ Incorrect! Try to remember the concept breakdown.")
                st.session_state.hearts = max(0, st.session_state.hearts - 1)

elif page == "Markets":
    st.title("Markets")
    st.info("Live market data feed active.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.info("Simulated trade execution engine ready.")
