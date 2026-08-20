import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TradeX - Duolingo Style Academy",
    page_icon="📈",
    layout="wide"
)

# Initialize Session State for Gamification, Progress, & Scoreboard
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
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (Duolingo Mode)", "Global Scoreboard", "Markets", "Paper Trading"])

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

    # Database with 5 questions per lesson
    lessons_db = {
        "Day 1: What is a Market Maker?": {
            "concept": "Market makers provide liquidity by always being ready to buy or sell at publicly quoted prices, earning revenue through the bid-ask spread.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["To crash the price", "To provide liquidity and facilitate trades", "To charge high trading taxes", "To print money"], "answer": "To provide liquidity and facilitate trades"},
                {"question": "What term describes the price difference between what buyers want to pay and sellers want to accept?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "Who typically acts as market makers in traditional stock markets?", "options": ["Individual retail traders", "Specialized institutional firms and designated specialists", "Central governments exclusively", "Cryptocurrency miners"], "answer": "Specialized institutional firms and designated specialists"},
                {"question": "How do market makers generally make a profit?", "options": ["By collecting transaction taxes", "Through the spread between bid and ask prices", "By shorting every retail account", "They operate purely as charities"], "answer": "Through the spread between bid and ask prices"},
                {"question": "What typically happens to market liquidity if market makers suddenly step away?", "options": ["Spreads widen and execution becomes difficult", "Prices freeze permanently", "Trading volume doubles instantly", "Fees drop to zero"], "answer": "Spreads widen and execution becomes difficult"}
            ]
        },
        "Day 2: Support & Resistance": {
            "concept": "Support is a price floor where buying interest overwhelms selling pressure, while resistance is a ceiling where selling pressure halts upward momentum.",
            "questions": [
                {"question": "When price hits a 'Resistance' level, what usually happens?", "options": ["Sellers step in and push price down", "Buyers panic and buy everything", "The exchange shuts down", "Nothing changes"], "answer": "Sellers step in and push price down"},
                {"question": "How is a 'Support' level viewed in technical analysis?", "options": ["A price ceiling", "A price floor where buying interest is strong", "A guaranteed loss point", "An indicator of bankruptcy"], "answer": "A price floor where buying interest is strong"},
                {"question": "What often happens when a major resistance level is broken with high volume?", "options": ["It flips into a new support level", "The asset gets delisted", "Trading is suspended for a week", "Volume drops to zero"], "answer": "It flips into a new support level"},
                {"question": "Why do round psychological numbers (like $50,000) often act as support or resistance?", "options": ["Because algorithms ignore them", "Because many human traders place orders at clean levels", "They never act as barriers", "Government regulations mandate it"], "answer": "Because many human traders place orders at clean levels"},
                {"question": "What is a 'false breakout' or 'liquidity sweep'?", "options": ["When a broker steals funds", "When price briefly spikes past a level to trigger stops before reversing", "A permanent market crash", "An error on the screen"], "answer": "When price briefly spikes past a level to trigger stops before reversing"}
            ]
        },
        "Day 3: The Hammer Candlestick": {
            "concept": "A hammer has a small body and a long lower wick, indicating that sellers tried to push prices down during the session, but buyers aggressively rejected it.",
            "questions": [
                {"question": "What does a long lower wick on a Hammer candle tell you?", "options": ["Extreme selling panic", "Price rejection and buyer defense", "Market closure", "Zero volume"], "answer": "Price rejection and buyer defense"},
                {"question": "What kind of body size is characteristic of a classic Hammer candle?", "options": ["A massive body spanning the whole day", "A small body located near the upper end of the range", "No body at all", "A perfectly square body"], "answer": "A small body located near the upper end of the range"},
                {"question": "Where do you typically look for a Hammer pattern to signal a potential bullish reversal?", "options": ["At the very top of a massive bull run", "At the bottom of a downtrend near support", "In the middle of a sideways flat range", "On a 5-second chart only"], "answer": "At the bottom of a downtrend near support"},
                {"question": "What color can the body of a valid hammer candle be?", "options": ["Only neon green", "Only dark red", "Either green or red", "Must be completely transparent"], "answer": "Either green or red"},
                {"question": "What is the core market psychology story behind a Hammer candle?", "options": ["Bears dominated every minute", "Bulls drove prices down all day", "Bears pushed prices low, but bulls bought up the dip before close", "Traders refused to participate"], "answer": "Bears pushed prices low, but bulls bought up the dip before close"}
            ]
        }
    }

    if st.session_state.active_lesson is None:
        st.title("🎯 Daily Missions & Progress Map")
        st.write("Complete each daily mission to fill your progress bar and level up your XP!")
        
        # Overall Academy Progress Calculation
        total_lessons = len(lessons_db)
        completed_count = len(st.session_state.completed_lessons)
        overall_progress = completed_count / total_lessons
        
        st.markdown("### Overall Curriculum Completion")
        st.progress(overall_progress)
        st.write(f"Completed {completed_count} of {total_lessons} modules.")
        st.markdown("---")
        
        for lesson_title, data in lessons_db.items():
            col1, col2 = st.columns([4, 1])
            with col1:
                is_done = lesson_title in st.session_state.completed_lessons
                status_icon = "✅ " if is_done else "🔒 "
                st.markdown(f"### {status_icon}{lesson_title}")
                st.write(data["concept"])
            with col2:
                btn_label = "Review 🔄" if lesson_title in st.session_state.completed_lessons else "Start Lesson 🚀"
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
        
        if st.button("⬅️ Back to Map"):
            st.session_state.active_lesson = None
            st.session_state.question_index = 0
            st.rerun()
            
        st.title(f"📖 {lesson_key}")
        
        # Lesson-specific progress bar
        lesson_progress = q_idx / total_q
        st.progress(lesson_progress)
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
                st.session_state.xp += 10
                
                if q_idx + 1 < total_q:
                    st.session_state.question_index += 1
                    if st.button("Next Question ➡️"):
                        st.rerun()
                else:
                    st.balloons()
                    st.success("🏆 Mission Completed! Full XP Awarded!")
                    st.session_state.completed_lessons.add(lesson_key)
                    st.session_state.active_lesson = None
                    st.session_state.question_index = 0
            else:
                st.error("❌ Incorrect! Try again.")
                st.session_state.hearts = max(0, st.session_state.hearts - 1)

elif page == "Global Scoreboard":
    st.title("🏆 TradeX Global Scoreboard")
    st.write("Top traders ranked by XP earned in the Trading Academy.")
    
    # Static global scoreboard mock data combined with live user XP
    scoreboard_data = pd.DataFrame([
        {"Rank": 1, "Trader": "CryptoAlpha", "XP": 1450, "Streak": 21},
        {"Rank": 2, "Trader": "BullishSzn", "XP": 1280, "Streak": 14},
        {"Rank": 3, "Trader": "Satoshi_99", "XP": 1100, "Streak": 9},
        {"Rank": 4, "Trader": "You (TradeX User)", "XP": st.session_state.xp, "Streak": st.session_state.streak},
        {"Rank": 5, "Trader": "TrendMaster", "XP": 890, "Streak": 5}
    ]).sort_values(by="XP", ascending=False).reset_index(drop=True)
    
    scoreboard_data["Rank"] = scoreboard_data.index + 1
    st.table(scoreboard_data)

elif page == "Markets":
    st.title("Markets")
    st.info("Live market data feed active.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.info("Simulated trade execution engine ready.")
    
