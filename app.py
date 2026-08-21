import streamlit as st
import pandas as pd
import numpy as np

# If curriculum.py is in the same folder as app.py:
from curriculum import lessons_db


# Page Configuration
st.set_page_config(
    page_title="TradeX - 3-Month Trading Academy",
    page_icon="📈",
    layout="wide"
)

# Initialize Session State Variables safely
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
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# Custom Modern Styling (TradingView / Dark Theme)
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
page = st.sidebar.radio(
    "Navigation", 
    ["Dashboard", "Trading Academy (3-Month Roadmap)", "Analytics", "Global Scoreboard", "Markets", "Paper Trading"]
)

# Sidebar Academy Progress Tracker
if len(lessons_db) > 0:
    progress_val = len(st.session_state.completed_lessons) / len(lessons_db)
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Academy Progress**")
    st.sidebar.progress(progress_val)
    st.sidebar.caption(f"{len(st.session_state.completed_lessons)} of {len(lessons_db)} modules completed")

# --- 1. DASHBOARD ---
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

# --- 2. TRADING ACADEMY ---
elif page == "Trading Academy (3-Month Roadmap)":
    st.markdown(f"""
        <div class="duo-stats">
            <span>🔥 Streak: {st.session_state.streak} Days</span>
            <span>⚡ XP: {st.session_state.xp}</span>
            <span>❤️ Hearts: {'❤️' * st.session_state.hearts}</span>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.active_lesson is None:
        st.subheader("Curriculum Roadmap")
        cols = st.columns(3)
        for i, (lesson_name, lesson_data) in enumerate(lessons_db.items()):
            col = cols[i % 3]
            is_completed = lesson_name in st.session_state.completed_lessons
            button_label = f"✅ {lesson_name}" if is_completed else lesson_name
            
            if col.button(button_label, key=f"btn_{i}", use_container_width=True):
                st.session_state.active_lesson = lesson_name
                st.session_state.question_index = 0
                st.session_state.feedback = None
                st.rerun()
    else:
        lesson = lessons_db[st.session_state.active_lesson]
        st.markdown(f"## {st.session_state.active_lesson}")
        st.info(f"**Concept Focus:** {lesson['concept']}")
        
        q_idx = st.session_state.question_index
        if q_idx < len(lesson['questions']):
            q = lesson['questions'][q_idx]
            st.markdown(f'<div class="quiz-box"><h4>Question {q_idx + 1} of {len(lesson["questions"])}</h4><p style="font-size: 1.1em; font-weight: 500;">{q["question"]}</p>', unsafe_allow_html=True)
            
            choice = st.radio("Select an option:", q['options'], key=f"q_{q_idx}")
            
            if st.session_state.feedback is None:
                if st.button("Submit Answer", type="primary"):
                    if choice == q['answer']:
                        st.session_state.feedback = ("correct", q['answer'])
                        st.session_state.xp += 10
                    else:
                        st.session_state.feedback = ("wrong", q['answer'])
                        st.session_state.hearts = max(0, st.session_state.hearts - 1)
                    st.rerun()
            else:
                status, correct_ans = st.session_state.feedback
                if status == "correct":
                    st.success("✅ **Correct!** Great deduction.")
                else:
                    st.error(f"❌ **Incorrect.** The correct answer was: **{correct_ans}**")
                
                if st.button("Next Question ➔", type="primary"):
                    st.session_state.feedback = None
                    st.session_state.question_index += 1
                    st.rerun()
                    
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.success("🎉 **Lesson Complete!** You've mastered this module and earned bonus XP.")
            st.session_state.completed_lessons.add(st.session_state.active_lesson)
            st.session_state.feedback = None
            if st.button("Return to Roadmap"):
                st.session_state.active_lesson = None
                st.rerun()

# --- 3. PERFORMANCE ANALYTICS ---
elif page == "Analytics":
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>PERFORMANCE METRICS</p>", unsafe_allow_html=True)
    st.title("Trading Analytics & Win-Rate Breakdown")
    
    np.random.seed(42)
    trade_dates = pd.date_range(start="2026-06-01", periods=20, freq="B")
    mock_trades = pd.DataFrame({
        "Date": trade_dates,
        "Asset": np.random.choice(["BTC", "ETH", "AAPL", "TSLA", "EUR/USD"], size=20),
        "Type": np.random.choice(["Long", "Short"], size=20),
        "P&L ($)": np.random.uniform(-150, 350, size=20).round(2),
        "Return (%)": np.random.uniform(-2.5, 5.0, size=20).round(2)
    })
    
    total_trades = len(mock_trades)
    winning_trades = len(mock_trades[mock_trades["P&L ($)"] > 0])
    win_rate = (winning_trades / total_trades) * 100
    net_profit = mock_trades["P&L ($)"].sum()
    gross_win = mock_trades[mock_trades["P&L ($)"] > 0]["P&L ($)"].sum()
    gross_loss = abs(mock_trades[mock_trades["P&L ($)"] < 0]["P&L ($)"].sum())
    profit_factor = gross_win / gross_loss if gross_loss > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Win Rate</p><h2 style="margin: 0; color: #ffffff;">{win_rate:.1f}%</h2><span style="color: #089981;">{winning_trades} Wins / {total_trades - winning_trades} Losses</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Net Profit / Loss</p><h2 style="margin: 0; color: { "#089981" if net_profit >= 0 else "#f23645" };">${net_profit:,.2f}</h2><span style="color: #848e9c;">Overall P&L</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Profit Factor</p><h2 style="margin: 0; color: #ffffff;">{profit_factor:.2f}</h2><span style="color: #089981;">Gross Win / Gross Loss</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Total Trades</p><h2 style="margin: 0; color: #ffffff;">{total_trades}</h2><span style="color: #848e9c;">Executed orders</span></div>', unsafe_allow_html=True)

    st.write("")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("### Cumulative Equity Curve")
        mock_trades["Cumulative P&L"] = mock_trades["P&L ($)"].cumsum()
        st.line_chart(mock_trades.set_index("Date")["Cumulative P&L"], color="#2962ff", height=300)
        
    with chart_col2:
        st.markdown("### P&L Distribution by Asset")
        asset_summary = mock_trades.groupby("Asset")["P&L ($)"].sum()
        st.bar_chart(asset_summary, color="#089981", height=300)

    st.markdown("### Recent Trade History")
    st.dataframe(
        mock_trades.style.map(
            lambda v: 'color: #089981' if isinstance(v, (int, float)) and v > 0 else ('color: #f23645' if isinstance(v, (int, float)) and v < 0 else ''),
            subset=["P&L ($)", "Return (%)"]
        ),
        use_container_width=True
    )

# --- 4. GLOBAL SCOREBOARD ---
elif page == "Global Scoreboard":
    st.title("Global Scoreboard")
    df = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "Trader": ["AlphaTrader", "MarketWizard", "CryptoKing", "RiskManager", "You"],
        "XP": [5400, 5200, 4800, 4500, st.session_state.xp],
        "Win Rate": ["82%", "79%", "75%", "72%", "68%"]
    })
    st.table(df)

# --- 5. MARKETS ---
elif page == "Markets":
    st.title("Market Overview")
    st.write("Real-time market data integration would appear here.")

# --- 6. PAPER TRADING ---
elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.write("Practice your skills with $10,000 of virtual capital.")
    
    ticker = st.text_input("Enter Ticker", "BTC")
    amount = st.number_input("Amount ($)", 100, 10000, value=1000)
    if st.button("Execute Trade", type="primary"):
        st.success(f"Simulated order placed successfully for ${amount:,.2f} of {ticker}!")
                      
