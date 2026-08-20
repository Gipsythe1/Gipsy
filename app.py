import streamlit as st
import pandas as pd
import numpy as np

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

    # Simplified, Clean Database Structure
    lessons_db = {
        "Month 1, Week 1: Market Mechanics": {
            "concept": "Mastering order types (Market, Limit, Stop) and exchange execution mechanics.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["Crash price", "Provide liquidity", "Charge taxes", "Print money"], "answer": "Provide liquidity"},
                {"question": "What describes the price difference between buyers and sellers?", "options": ["Leverage", "Bid-Ask Spread", "Dividend", "Fee"], "answer": "Bid-Ask Spread"},
                {"question": "Which order guarantees speed over price?", "options": ["Limit", "Market", "Stop", "GTC"], "answer": "Market"}
            ]
        },
        "Month 1, Week 2: Support & Resistance": {
            "concept": "Identifying structural turning points where market participants dominate price action.",
            "questions": [
                {"question": "What happens when price hits Resistance?", "options": ["Sellers push price down", "Buyers panic", "Exchange shuts down", "Nothing"], "answer": "Sellers push price down"},
                {"question": "What is a Support level?", "options": ["Price ceiling", "Price floor where buying is strong", "Loss point", "Bankruptcy indicator"], "answer": "Price floor where buying is strong"}
            ]
        },
        "Month 2, Week 5: Moving Averages": {
            "concept": "Utilizing Simple and Exponential Moving Averages (SMA/EMA).",
            "questions": [
                {"question": "What is the key difference with EMA?", "options": ["Weights recent prices more", "Only for crypto", "Lags further", "No difference"], "answer": "Weights recent prices more"},
                {"question": "What is a Golden Cross?", "options": ["Short MA crosses above long MA", "Price drops 50%", "Tax rule", "Candle pattern"], "answer": "Short MA crosses above long MA"}
            ]
        },
        "Month 3, Week 11: Trading Journals": {
            "concept": "Tracking win rates, risk-reward expectancy, and finding edge through data.",
            "questions": [
                {"question": "Why keep a trading journal?", "options": ["To log mistakes and analyze edge", "To show friends", "Tax compliance", "Pass time"], "answer": "To log mistakes and analyze edge"},
                {"question": "What is trading Expectancy?", "options": ["Average amount won/lost per dollar risked", "Emotional mood", "Daily profit goal", "Guaranteed return"], "answer": "Average amount won/lost per dollar risked"}
            ]
        }
    }

    if st.session_state.active_lesson is None:
        st.title("🎯 3-Month Masterclass Curriculum Roadmap")
        st.write("Complete weekly modules to master markets from scratch.")
        
        total_lessons = len(lessons_db)
        completed_count = len(st.session_state.completed_lessons)
        st.markdown(f"### Overall Academy Progress ({completed_count}/{total_lessons} Completed)")
        st.progress(completed_count / total_lessons if total_lessons > 0 else 0)
        st.markdown("---")
        
        for lesson_title, data in lessons_db.items():
            col1, col2 = st.columns([4, 1])
            with col1:
                is_done = lesson_title in st.session_state.completed_lessons
                status_icon = "✅ " if is_done else "🔒 "
                st.markdown(f"### {status_icon}{lesson_title}")
                st.write(data["concept"])
            with col2:
                btn_label = "Review 🔄" if is_done else "Start Module 🚀"
                if st.button(btn_label, key=lesson_title):
                    st.session_state.active_lesson = lesson_title
                    st.session_state.question_index = 0
                    st.rerun()
            st.markdown("---")
            
    else:
        lesson_key = st.session_state.active_lesson
        current_lesson = lessons_db[lesson_key]
        q_idx = st.session_state.question_index
        total_q = len(current_lesson['questions'])
        
        if st.button("⬅️ Back to Roadmap"):
            st.session_state.active_lesson = None
            st.session_state.question_index = 0
            st.rerun()
            
        st.title(f"📖 {lesson_key}")
        st.progress(q_idx / total_q)
        st.write(f"Question {q_idx + 1} of {total_q}")
        
        q_data = current_lesson["questions"][q_idx]
        
        st.markdown(f"""
        <div class="quiz-box">
            <h4 style="color: #2962ff;">🧩 Challenge</h4>
            <p style="font-size: 1.1rem; font-weight: bold;">{q_data['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        user_choice = st.radio("Select your answer:", q_data["options"], key=f"q_{q_idx}")
        
        if st.button("Check Answer ✅"):
            if user_choice == q_data["answer"]:
                st.success("🎉 Correct! Great job!")
                st.session_state.xp += 15
                
                if q_idx + 1 < total_q:
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    st.balloons()
                    st.success("🏆 Module Completed!")
                    st.session_state.completed_lessons.add(lesson_key)
                    st.session_state.active_lesson = None
                    st.session_state.question_index = 0
            else:
                st.error("❌ Incorrect! Try again.")
                st.session_state.hearts = max(0, st.session_state.hearts - 1)

elif page == "Global Scoreboard":
    st.title("🏆 TradeX Global Scoreboard")
    scoreboard_data = pd.DataFrame([
        {"Rank": 1, "Trader": "CryptoAlpha", "XP": 3450, "Streak": 45},
        {"Rank": 2, "Trader": "BullishSzn", "XP": 2980, "Streak": 30},
        {"Rank": 3, "Trader": "You (TradeX User)", "XP": st.session_state.xp, "Streak": st.session_state.streak}
    ])
    st.table(scoreboard_data)

elif page == "Markets":
    st.title("Markets")
    st.info("Live market data feed active.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.info("Simulated trade execution engine ready.")
        
