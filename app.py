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

    # 3-Month Curriculum Structured by Weeks & Days
    lessons_db = {
        # Month 1, Week 1
        "M1 W1 D1: Bid-Ask Spreads": {
            "concept": "Order books, market makers, and liquidity.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["Crash price", "Provide liquidity", "Charge high taxes", "Print money"], "answer": "Provide liquidity"},
                {"question": "What term describes the gap between buyers and sellers?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "What happens to spreads during high volatility?", "options": ["Tighten", "Widen significantly", "Disappear", "Pause"], "answer": "Widen significantly"},
                {"question": "Who absorbs market orders on an exchange?", "options": ["Limit orders in the book", "Government", "Miners", "Random generators"], "answer": "Limit orders in the book"},
                {"question": "What is market depth?", "options": ["Ocean depth", "Volume of pending orders", "Account balance", "Leverage limit"], "answer": "Volume of pending orders"}
            ]
        },
        "M1 W1 D2: Market vs Limit Orders": {
            "concept": "Execution speed versus price precision.",
            "questions": [
                {"question": "Which order guarantees execution speed?", "options": ["Limit Order", "Market Order", "Stop-Loss", "GTC Order"], "answer": "Market Order"},
                {"question": "What is a Limit Order used for?", "options": ["Instant execution", "Specifying exact target price", "Closing account", "Avoiding taxes"], "answer": "Specifying exact target price"},
                {"question": "What is slippage?", "options": ["Ice on chart", "Difference between expected and execution price", "Broker bonus", "Platform crash"], "answer": "Difference between expected and execution price"},
                {"question": "When should you prefer a Limit Order?", "options": ["Low liquidity or avoiding slippage", "During panic crash", "Never", "100x leverage"], "answer": "Low liquidity or avoiding slippage"},
                {"question": "What does IOC mean?", "options": ["Cancel account", "Execute immediately or cancel", "Ignore conditions", "Infinite orders"], "answer": "Execute immediately or cancel"}
            ]
        },
        "M1 W1 D3: Stop Orders": {
            "concept": "Conditional trigger orders for risk control.",
            "questions": [
                {"question": "What triggers a Stop-Loss?", "options": ["Price reaching trigger price", "Manual click", "Random timer", "Volume drop"], "answer": "Price reaching trigger price"},
                {"question": "What is a Stop-Limit order?", "options": ["Turns into limit order when triggered", "Permanent ban", "Free trade", "Market order"], "answer": "Turns into limit order when triggered"},
                {"question": "Why use a Stop-Loss?", "options": ["Limit potential trading losses automatically", "Guarantee profit", "Increase fees", "Double margin"], "answer": "Limit potential trading losses automatically"},
                {"question": "Can a Stop-Limit order fail?", "options": ["Never", "Yes, if price moves past limit too fast", "Only weekends", "Only crypto"], "answer": "Yes, if price moves past limit too fast"},
                {"question": "What is a Trailing Stop?", "options": ["Tracks favorable price movement", "Lagging indicator", "Fixed floor", "Market exit"], "answer": "Tracks favorable price movement"}
            ]
        },
        "M1 W1 D4: Margin & Leverage": {
            "concept": "Amplifying position exposure with borrowed capital.",
            "questions": [
                {"question": "What is leverage?", "options": ["Borrowing funds to increase position size", "Physical tool", "Tax penalty", "Chart type"], "answer": "Borrowing funds to increase position size"},
                {"question": "What is a Margin Call?", "options": ["Phone call", "Demand to add collateral funds", "Winning prize", "Closing trade"], "answer": "Demand to add collateral funds"},
                {"question": "What happens with 10x leverage on a 10% adverse move?", "options": ["Break even", "Liquidation (total loss)", "Double money", "Nothing"], "answer": "Liquidation (total loss)"},
                {"question": "What is initial margin?", "options": ["Collateral required to open position", "Free money", "Broker fee", "Profit target"], "answer": "Collateral required to open position"},
                {"question": "Is high leverage recommended for beginners?", "options": ["Always", "No, it destroys accounts", "Fridays", "Stocks only"], "answer": "No, it destroys accounts"}
            ]
        },
        "M1 W1 D5: Exchange Architecture": {
            "concept": "Centralized vs decentralized exchange mechanics.",
            "questions": [
                {"question": "What is a CEX?", "options": ["Company-managed order matching platform", "P2P network", "Bank vault", "Chart pattern"], "answer": "Company-managed order matching platform"},
                {"question": "What is a DEX?", "options": ["Smart contract exchange on blockchain", "Physical floor", "Closed DB", "Stock broker"], "answer": "Smart contract exchange on blockchain"},
                {"question": "What does T+1 settlement mean?", "options": ["Trades settle one day after execution", "One year", "Instant cash", "Zero settlement"], "answer": "Trades settle one day after execution"},
                {"question": "What is counterparty risk?", "options": ["Risk that party or exchange fails to fulfill", "Market volatility", "Slippage", "Spread cost"], "answer": "Risk that party or exchange fails to fulfill"},
                {"question": "What is cold storage?", "options": ["Refrigerator", "Offline wallet security", "Trading strategy", "Downturn"], "answer": "Offline wallet security"}
            ]
        },
        # Additional Month 1 Weeks (2, 3, 4) & Months 2-3 summarized
        "M1 W2 D1: Support Floors": {
            "concept": "Finding historical price levels where buying occurs.",
            "questions": [
                {"question": "What is a Support level?", "options": ["Price ceiling", "Price floor where buyers step in", "Guaranteed profit", "Tax bracket"], "answer": "Price floor where buyers step in"},
                {"question": "Why do support zones work?", "options": ["Traders remember historical reaction points", "Magic", "Government", "Random chance"], "answer": "Traders remember historical reaction points"},
                {"question": "What makes support more reliable?", "options": ["1 touch", "Multiple touches over time", "Zero touches", "1000 touches"], "answer": "Multiple touches over time"},
                {"question": "What happens when price breaks support?", "options": ["Accelerates downward", "Bounces to infinity", "Stops", "Nothing"], "answer": "Accelerates downward"},
                {"question": "Where to place stop loss?", "options": ["On line", "Just below support zone", "At top", "No stops"], "answer": "Just below support zone"}
            ]
        },
        "M1 W3 D1: Candlestick Rejections": {
            "concept": "Decoding wicks for reversal signals.",
            "questions": [
                {"question": "What does a long lower wick on a Hammer indicate?", "options": ["Price rejection and buyer defense", "Extreme selling", "Closure", "Zero volume"], "answer": "Price rejection and buyer defense"},
                {"question": "Where should a Hammer appear?", "options": ["Bottom of downtrend near support", "Top of bull run", "Flat chop", "1s chart"], "answer": "Bottom of downtrend near support"},
                {"question": "What is a Shooting Star?", "options": ["Bearish reversal candle at resistance", "Bullish breakout", "Moving average", "Volume spike"], "answer": "Bearish reversal candle at resistance"},
                {"question": "What is body size of a hammer?", "options": ["Small body near upper range", "Massive", "None", "Square"], "answer": "Small body near upper range"},
                {"question": "Why are wicks crucial?", "options": ["Show price rejection extremes", "Random noise", "Calculate taxes", "Set fees"], "answer": "Show price rejection extremes"}
            ]
        },
        "M1 W4 D1: Bull Market Structure": {
            "concept": "Higher highs and higher lows expansion.",
            "questions": [
                {"question": "What defines a Bull Market structure?", "options": ["Sequence of Higher Highs and Higher Lows", "Lower lows", "Flat chop", "Crashes"], "answer": "Sequence of Higher Highs and Higher Lows"},
                {"question": "What is a Higher Low?", "options": ["Pullback stopping higher than previous correction", "Crash low", "MA", "Resistance"], "answer": "Pullback stopping higher than previous correction"},
                {"question": "When is uptrend intact?", "options": ["As long as unbroken Higher Lows continue", "Positive news", "Confidence", "Zero volume"], "answer": "As long as unbroken Higher Lows continue"},
                {"question": "What if price fails to make Higher High?", "options": ["Warning of trend fatigue", "Guaranteed moon", "Upgrade", "Refund"], "answer": "Warning of trend fatigue"},
                {"question": "How to trade uptrends?", "options": ["Buy pullbacks near support", "Sell green", "100x short", "Never"], "answer": "Buy pullbacks near support"}
            ]
        },
        "Month 2, Week 5: Moving Averages": {
            "concept": "SMA, EMA, and cross indicators.",
            "questions": [
                {"question": "Key difference with EMA?", "options": ["Weights recent prices more", "Crypto only", "Lags more", "No difference"], "answer": "Weights recent prices more"},
                {"question": "What is a Golden Cross?", "options": ["Short MA crosses above long MA", "Price drop", "Tax rule", "Pattern"], "answer": "Short MA crosses above long MA"},
                {"question": "What does a Death Cross signify?", "options": ["Bearish momentum", "Bull run", "Close", "High volume"], "answer": "Bearish momentum"},
                {"question": "How do traders use MAs?", "options": ["Dynamic support and resistance", "Predict exact prices", "Taxes", "Decoration"], "answer": "Dynamic support and resistance"},
                {"question": "Common pitfall in choppy markets?", "options": ["False whipsaw signals", "Break screens", "Zero data", "High fees"], "answer": "False whipsaw signals"}
            ]
        },
        "Month 3, Week 11: Trading Journals": {
            "concept": "Tracking win rates and expectancy.",
            "questions": [
                {"question": "Why keep a journal?", "options": ["Log mistakes and analyze edge", "Show friends", "Tax", "Pass time"], "answer": "Log mistakes and analyze edge"},
                {"question": "What is Expectancy?", "options": ["Average amount won/lost per dollar risked", "Mood", "Daily goal", "Return"], "answer": "Average amount won/lost per dollar risked"},
                {"question": "Can 40% win rate be profitable?", "options": ["Yes, with high risk-reward ratio", "No, must be 100%", "Forex only", "Never"], "answer": "Yes, with high risk-reward ratio"},
                {"question": "What metric measures plan compliance?", "options": ["Plan Adherence Score", "Balance alone", "Speed", "Count"], "answer": "Plan Adherence Score"},
                {"question": "How often to review logs?", "options": ["Weekly or monthly", "Every 10 years", "Never", "Bankruptcy"], "answer": "Weekly or monthly"}
            ]
        }
    }

    if st.session_state.active_lesson is None:
        st.title("🎯 3-Month Masterclass Curriculum Roadmap")
        st.write("Complete daily modules to master market mechanics, price action, and trading psychology.")
        
        total_lessons = len(lessons_db)
        completed_count = len(st.session_state.completed_lessons)
        progress_val = completed_count / total_lessons if total_lessons > 0 else 0
        
        st.markdown(f"### Overall Academy Progress ({completed_count}/{total_lessons} Modules Completed)")
        st.progress(progress_val)
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
    
