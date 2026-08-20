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
        st.markdown('<div class="metric-card"><p style="color: &848e9c; margin-bottom: 5px;">Available Cash</p><h2 style="margin: 0; color: #ffffff;">$8,750.00</h2><span style="color: #848e9c;">Ready to trade</span></div>', unsafe_allow_html=True)

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

    # Full 3-Month Curriculum (Months 1, 2, and 3) Structured by Weeks
    lessons_db = {
        # ==================== MONTH 1: MARKET MECHANICS & PRICE ACTION ====================
        "M1 W1 D1: Bid-Ask Spreads": {
            "concept": "Order books, market makers, and liquidity mechanics.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["Crash price", "Provide liquidity", "Charge high taxes", "Print money"], "answer": "Provide liquidity"},
                {"question": "What term describes the gap between buyers and sellers?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "What happens to spreads during high volatility?", "options": ["Tighten", "Widen significantly", "Disappear", "Pause"], "answer": "Widen significantly"},
                {"question": "Who absorbs market orders on an exchange?", "options": ["Limit orders in the book", "Government", "Miners", "Random generators"], "answer": "Limit orders in the book"},
                {"question": "What is market depth?", "options": ["Ocean depth", "Volume of pending orders", "Account balance", "Leverage limit"], "answer": "Volume of pending orders"}
            ]
        },
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

        # ==================== MONTH 2: TECHNICAL INDICATORS & OSCILLATORS ====================
        "M2 W5 D1: Simple vs Exponential Moving Averages": {
            "concept": "Mastering SMA and EMA calculations and smoothing.",
            "questions": [
                {"question": "What is the core difference between SMA and EMA?", "options": ["EMA weights recent prices heavier", "SMA is only for stocks", "EMA has no lag", "No difference"], "answer": "EMA weights recent prices heavier"},
                {"question": "Why do traders use the 200-day moving average?", "options": ["As a long-term macro trend filter", "To calculate daily taxes", "To pick exact bottoms", "For fun"], "answer": "As a long-term macro trend filter"},
                {"question": "What is a Moving Average crossover signal?", "options": ["When a fast MA crosses a slow MA", "Broker system crash", "Market closure", "Zero volume"], "answer": "When a fast MA crosses a slow MA"},
                {"question": "What is a Death Cross?", "options": ["50 SMA crossing below 200 SMA", "Price dropping to zero", "Account liquidation", "Option expiry"], "answer": "50 SMA crossing below 200 SMA"},
                {"question": "What is the main drawback of Moving Averages?", "options": ["They lag behind current price action", "They predict the future", "They cost high fees", "They never work"], "answer": "They lag behind current price action"}
            ]
        },
        "M2 W6 D1: Relative Strength Index (RSI)": {
            "concept": "Evaluating overbought and oversold momentum conditions.",
            "questions": [
                {"question": "What does an RSI reading above 70 typically indicate?", "options": ["Overbought conditions with potential pullback risk", "Oversold extreme buy", "Market crash", "Zero volatility"], "answer": "Overbought conditions with potential pullback risk"},
                {"question": "What is RSI divergence?", "options": ["Price making higher highs while RSI makes lower highs", "Price matching RSI", "Broker glitch", "Margin call"], "answer": "Price making higher highs while RSI makes lower highs"},
                {"question": "What is the standard RSI lookback period?", "options": ["14 periods", "100 periods", "1 period", "50 periods"], "answer": "14 periods"},
                {"question": "Can an asset stay overbought for a long time during strong trends?", "options": ["Yes, strong trends defy standard RSI thresholds", "No, it must crash instantly", "Only on weekends", "Never"], "answer": "Yes, strong trends defy standard RSI thresholds"},
                {"question": "What does RSI measure?", "options": ["Magnitude of recent price changes to evaluate velocity", "Trading volume", "Account balance", "Leverage ratio"], "answer": "Magnitude of recent price changes to evaluate velocity"}
            ]
        },
        "M2 W7 D1: MACD & Momentum Convergence": {
            "concept": "Moving Average Convergence Divergence histogram analysis.",
            "questions": [
                {"question": "What does MACD stand for?", "options": ["Moving Average Convergence Divergence", "Market Asset Cash Distributor", "Margin Asset Calculation Device", "Moving Action Currency Direction"], "answer": "Moving Average Convergence Divergence"},
                {"question": "What generates a bullish MACD crossover signal?", "options": ["MACD line crosses above the signal line", "MACD equals zero", "Volume disappears", "Price drops"], "answer": "MACD line crosses above the signal line"},
                {"question": "What does the MACD histogram measure?", "options": ["The distance between the MACD line and signal line", "Total exchange volume", "Open interest", "Account profit"], "answer": "The distance between the MACD line and signal line"},
                {"question": "How is the baseline MACD line calculated?", "options": ["Difference between 12-period EMA and 26-period EMA", "Simple average of volume", "High minus low", "Close divided by open"], "answer": "Difference between 12-period EMA and 26-period EMA"},
                {"question": "What indicates decreasing momentum on the MACD histogram?", "options": ["Bars shrinking toward the zero line", "Bars growing infinitely", "Color staying constant", "Zero lines moving"], "answer": "Bars shrinking toward the zero line"}
            ]
        },
        "M2 W8 D1: Bollinger Bands & Volatility Squeezes": {
            "concept": "Using standard deviation envelopes to trade breakouts.",
            "questions": [
                {"question": "What do Bollinger Bands consist of?", "options": ["A middle SMA and upper/lower standard deviation bands", "Three resistance lines", "Random indicators", "Volume bars"], "answer": "A middle SMA and upper/lower standard deviation bands"},
                {"question": "What is a Bollinger Band 'Squeeze'?", "options": ["Bands narrowing significantly due to low volatility compression", "Bands expanding", "Broker freezing account", "Margin call"], "answer": "Bands narrowing significantly due to low volatility compression"},
                {"question": "What usually follows a tight volatility squeeze?", "options": ["An explosive directional breakout move", "Market closure", "Zero volume forever", "Tax payment"], "answer": "An explosive directional breakout move"},
                {"question": "What does it mean when price hugs the upper Bollinger Band?", "options": ["Strong bullish momentum", "Extreme weakness", "Market crash", "Flat range"], "answer": "Strong bullish momentum"},
                {"question": "How are Bollinger Band standard deviations typically set?", "options": ["2 standard deviations from the 20-period SMA", "1 standard deviation from 10 SMA", "5 standard deviations", "No standard deviation"], "answer": "2 standard deviations from the 20-period SMA"}
            ]
        },

        # ==================== MONTH 3: RISK MANAGEMENT & ADVANCED STRATEGIES ====================
        "M3 W9 D1: Position Sizing & Risk Management": {
            "concept": "Protecting capital using the 1% rule and fixed fractional risk.",
            "questions": [
                {"question": "What is the core rule of risk management per trade?", "options": ["Risk only a small fixed percentage (e.g., 1-2%) of total capital", "Risk 100% on every trade", "Never use stop losses", "Borrow maximum leverage"], "answer": "Risk only a small fixed percentage (e.g., 1-2%) of total capital"},
                {"question": "How do you calculate position size?", "options": ["Account Risk Dollars divided by Distance to Stop Loss in dollars", "Random guess", "Account balance multiplied by 10", "Fee divided by leverage"], "answer": "Account Risk Dollars divided by Distance to Stop Loss in dollars"},
                {"question": "What is Risk-to-Reward Ratio (RRR)?", "options": ["Potential profit target distance compared to potential stop loss risk distance", "Broker fee ratio", "Leverage multiplier", "Win rate percentage"], "answer": "Potential profit target distance compared to potential stop loss risk distance"},
                {"question": "Why is a 1:3 Risk-to-Reward ratio powerful?", "options": ["You can be profitable even with a win rate below 40%", "It guarantees 100% wins", "It eliminates all market risk", "Brokers give bonuses"], "answer": "You can be profitable even with a win rate below 40%"},
                {"question": "What is 'ruin risk' in trading?", "options": ["The mathematical probability of losing your entire trading capital", "A minor losing streak", "A tax penalty", "A software glitch"], "answer": "The mathematical probability of losing your entire trading capital"}
            ]
        },
        "M3 W10 D1: Trading Psychology & Emotional Control": {
            "concept": "Overcoming FOMO, revenge trading, and cognitive biases.",
            "questions": [
                {"question": "What is 'Revenge Trading'?", "options": ["Taking impulsive, oversized trades to quickly win back previous losses", "Trading as a career", "Closing a winning trade", "Following your plan"], "answer": "Taking impulsive, oversized trades to quickly win back previous losses"},
                {"question": "What does FOMO stand for in trading?", "options": ["Fear Of Missing Out", "Future Order Market Option", "Fixed Overall Margin Outlay", "Fast Online Money Operation"], "answer": "Fear Of Missing Out"},
                {"question": "How do professional traders handle a losing streak?", "options": ["Step away from screens and adhere strictly to risk rules", "Double position size immediately", "Break computer", "Blame the market maker"], "answer": "Step away from screens and adhere strictly to risk rules"},
                {"question": "What is confirmation bias?", "options": ["Seeking out information that confirms your existing bias while ignoring warning signs", "Trading accurately", "Confirming account deposits", "Broker verification"], "answer": "Seeking out information that confirms your existing bias while ignoring warning signs"},
                {"question": "Why is keeping emotions detached crucial?", "options": ["Emotions lead to hesitation, breaking rules, and capital destruction", "Emotions increase leverage", "Brokers hate feelings", "It makes trading boring"], "answer": "Emotions lead to hesitation, breaking rules, and capital destruction"}
            ]
        },
        "M3 W11 D1: Trading Journals & Performance Analytics": {
            "concept": "Logging trades, win rates, and finding edge through data.",
            "questions": [
                {"question": "Why keep a trading journal?", "options": ["To log mistakes, analyze setup performance, and find your statistical edge", "To show friends", "Tax compliance", "Pass time"], "answer": "To log mistakes, analyze setup performance, and find your statistical edge"},
                {"question": "What is trading Expectancy?", "options": ["Average amount won/lost per dollar risked based on win rate and RRR", "Emotional mood", "Daily goal", "Guaranteed return"], "answer": "Average amount won/lost per dollar risked based on win rate and RRR"},
                {"question": "What metric measures how well you stick to your trading plan?", "options": ["Plan Adherence Score", "Account balance alone", "Click speed", "Trade count"], "answer": "Plan Adherence Score"},
                {"question": "How often should your journal logs be reviewed?", "options": ["Weekly or monthly to detect behavioral leaks and edge decay", "Every 10 years", "Never", "Only after bankruptcy"], "answer": "Weekly or monthly to detect behavioral leaks and edge decay"},
                {"question": "What key data fields should every journal include?", "options": ["Entry price, exit price, stop loss, setup type, emotional state, and screenshots", "Only account balance", "Favorite color", "Weather condition"], "answer": "Entry price, exit price, stop loss, setup type, emotional state, and screenshots"}
            ]
        },
        "M3 W12 D1: Building a Complete Trading Plan": {
            "concept": "Synthesizing edge, rules, routine, and execution into a master system.",
            "questions": [
                {"question": "What is the purpose of a written Trading Plan?", "options": ["To serve as an objective rulebook removing real-time decision fatigue", 
