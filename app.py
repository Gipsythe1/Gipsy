import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="TradeX - 3-Month Trading Academy", page_icon="📈", layout="wide")

if "xp" not in st.session_state: st.session_state.xp = 150
if "hearts" not in st.session_state: st.session_state.hearts = 5
if "streak" not in st.session_state: st.session_state.streak = 3
if "active_lesson" not in st.session_state: st.session_state.active_lesson = None
if "question_index" not in st.session_state: st.session_state.question_index = 0
if "completed_lessons" not in st.session_state: st.session_state.completed_lessons = set()

st.markdown("""
    <style>
    .stApp { background-color: #131722; color: #d1d4dc; }
    .metric-card { background-color: #1e222d; border: 1px solid #2a2e39; padding: 20px; border-radius: 10px; }
    .duo-stats { display: flex; justify-content: space-between; align-items: center; background: #1e222d; padding: 12px 20px; border-radius: 12px; border: 1px solid #2a2e39; margin-bottom: 20px; font-weight: bold; }
    .quiz-box { background-color: #1e222d; border: 1px solid #2a2e39; padding: 25px; border-radius: 16px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## TRADE<span style='color: #2962ff;'>X</span>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (3-Month Roadmap)", "Global Scoreboard", "Markets", "Paper Trading"])

if page == "Dashboard":
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>WELCOME BACK</p>", unsafe_allow_html=True)
    st.title("Trading Dashboard")
    
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Portfolio Value</p><h2 style="margin: 0; color: #ffffff;">$10,000.00</h2><span style="color: #089981; font-weight: bold;">+2.45%</span></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Today\'s Profit</p><h2 style="margin: 0; color: #ffffff;">$245.60</h2><span style="color: #089981; font-weight: bold;">+2.45%</span></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><p style="color: #848e9c; margin-bottom: 5px;">Available Cash</p><h2 style="margin: 0; color: #ffffff;">$8,750.00</h2><span style="color: #848e9c;">Ready to trade</span></div>', unsafe_allow_html=True)

    st.write("")
    chart_col, watch_col = st.columns([3, 1])
    with chart_col:
        st.markdown("### BTC / USD\n## $68,420.50")
        st.line_chart(pd.DataFrame(np.random.randn(50, 1).cumsum() + 68420, columns=["Price"]), color="#2962ff", height=350)
    with watch_col:
        st.markdown("### Watchlist")
        for asset, price in {"BTC": "$68,420", "ETH": "$3,420", "AAPL": "$227.10", "TSLA": "$341.20"}.items():
            st.markdown(f'<div style="background: #1e222d; padding: 12px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between;"><b>{asset}</b><span style="color: #848e9c;">{price}</span></div>', unsafe_allow_html=True)

elif page == "Trading Academy (3-Month Roadmap)":
    st.markdown(f'<div class="duo-stats"><span>🔥 Streak: {st.session_state.streak} Days</span><span>⚡ XP: {st.session_state.xp}</span><span>❤️ Hearts: {"❤️" * st.session_state.hearts}</span></div>', unsafe_allow_html=True)

    lessons_db = {
        "M1 W1: Market Mechanics & Orders": {
            "concept": "Mastering order books, market makers, spreads, and leverage mechanics.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["Crash price", "Provide liquidity", "Charge high taxes", "Print money"], "answer": "Provide liquidity"},
                {"question": "What term describes the gap between buyers and sellers?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "Which order guarantees execution speed over price?", "options": ["Limit Order", "Market Order", "Stop-Loss", "GTC Order"], "answer": "Market Order"},
                {"question": "What happens with 10x leverage on a 10% adverse move?", "options": ["Break even", "Liquidation (total loss)", "Double money", "Nothing"], "answer": "Liquidation (total loss)"},
                {"question": "What is market depth?", "options": ["Ocean depth", "Volume of pending orders", "Account balance", "Leverage limit"], "answer": "Volume of pending orders"}
            ]
        },
        "M1 W2: Support & Resistance Zones": {
            "concept": "Locating structural turning points and polarity swaps.",
            "questions": [
                {"question": "What is a Support level?", "options": ["Price ceiling", "Price floor where buyers step in", "Guaranteed profit", "Tax bracket"], "answer": "Price floor where buyers step in"},
                {"question": "What happens when price approaches Resistance?", "options": ["Sellers step in and push price down", "Buyers panic buy", "Volume disappears", "Exchanges close"], "answer": "Sellers step in and push price down"},
                {"question": "What is a polarity swap?", "options": ["When broken support turns into new resistance", "Broker glitch", "Tax swap", "Leverage flip"], "answer": "When broken support turns into new resistance"},
                {"question": "Why do round numbers act as barriers?", "options": ["Human psychological clustering of orders", "Code constraints", "Government limits", "Zero volume"], "answer": "Human psychological clustering of orders"},
                {"question": "How many swing points form a valid trendline?", "options": ["At least 2 points with a 3rd confirmation point", "1 point", "100 points", "Zero points"], "answer": "At least 2 points with a 3rd confirmation point"}
            ]
        },
        "M1 W3: Candlestick Pattern Recognition": {
            "concept": "Decoding wicks, engulfing bodies, and volatility compression.",
            "questions": [
                {"question": "What does a long lower wick on a Hammer indicate?", "options": ["Price rejection and buyer defense at lows", "Extreme selling", "Closure", "Zero volume"], "answer": "Price rejection and buyer defense at lows"},
                {"question": "What is a Bullish Engulfing pattern?", "options": ["A green candle whose body engulfs the prior red candle", "Small doji", "Crash indicator", "Low liquidity"], "answer": "A green candle whose body engulfs the prior red candle"},
                {"question": "What does a Doji candlestick represent?", "options": ["Open and close prices are virtually identical, showing indecision", "Strong buyers", "Strong sellers", "Guaranteed crash"], "answer": "Open and close prices are virtually identical, showing indecision"},
                {"question": "Where does a Morning Star pattern form?", "options": ["At the bottom of a downtrend", "At the top of a bull run", "Flat range", "5-second chart"], "answer": "At the bottom of a downtrend"},
                {"question": "What does an Inside Bar signify?", "options": ["Volatility contraction and market consolidation", "Massive panic", "Exchange crash", "Infinite volume"], "answer": "Volatility contraction and market consolidation"}
            ]
        },
        "M1 W4: Trend Structure & Momentum": {
            "concept": "Mapping higher highs, market cycles, and structure breaks.",
            "questions": [
                {"question": "What defines a healthy Bull Market structure?", "options": ["Sequence of Higher Highs and Higher Lows", "Lower lows", "Flat chop", "Crashes"], "answer": "Sequence of Higher Highs and Higher Lows"},
                {"question": "What is the 'Accumulation' phase?", "options": ["Smart money quietly buying assets in a sideways range", "Massive panic selling", "Retail FOMO buying", "Market closure"], "answer": "Smart money quietly buying assets in a sideways range"},
                {"question": "What is a CHoCH (Change of Character)?", "options": ["The first structural break indicating a potential trend reversal", "Moving average cross", "Exchange fee", "Candle pattern"], "answer": "The first structural break indicating a potential trend reversal"},
                {"question": "What is a Bear Market structure?", "options": ["Sequence of Lower Highs and Lower Lows", "Higher highs", "Parabolic pumps", "Zero volatility"], "answer": "Sequence of Lower Highs and Lower Lows"},
                {"question": "Why is multi-timeframe analysis necessary?", "options": ["To ensure lower timeframe trades align with higher timeframe trends", "To confuse traders", "Brokers require it", "No use"], "answer": "To ensure lower timeframe trades align with higher timeframe trends"}
            ]
        },
        "M2 W5: Moving Averages & Trend Filters": {
            "concept": "Utilizing SMA, EMA, and Golden/Death crosses.",
            "questions": [
                {"question": "What is the key difference with EMA?", "options": ["Weights recent prices more", "Only for crypto", "Lags further", "No difference"], "answer": "Weights recent prices more"},
                {"question": "What is a Golden Cross?", "options": ["Short MA crosses above long MA", "Price drops 50%", "Tax rule", "Candle pattern"], "answer": "Short MA crosses above long MA"},
                {"question": "What does a Death Cross signify?", "options": ["Bearish momentum when short MA crosses below long MA", "Bull run", "Exchange close", "High volume"], "answer": "Bearish momentum when short MA crosses below long MA"},
                {"question": "How do traders use MAs dynamically?", "options": ["As dynamic support and resistance", "To predict exact prices", "To pay taxes", "For decoration"], "answer": "As dynamic support and resistance"},
                {"question": "What is a common pitfall of MAs in choppy markets?", "options": ["Too many false whipsaw signals", "Break computer screens", "Zero data", "High fees"], "answer": "Too many false whipsaw signals"}
            ]
        },
        "M2 W6: Momentum Oscillators (RSI)": {
            "concept": "Evaluating overbought and oversold conditions with RSI divergence.",
            "questions": [
                {"question": "What does an RSI reading above 70 typically indicate?", "options": ["Overbought conditions with potential pullback risk", "Oversold buy", "Market crash", "Zero volatility"], "answer": "Overbought conditions with potential pullback risk"},
                {"question": "What is RSI divergence?", "options": ["Price making higher highs while RSI makes lower highs", "Price matching RSI", "Broker glitch", "Margin call"], "answer": "Price making higher highs while RSI makes lower highs"},
                {"question": "What is the standard RSI lookback period?", "options": ["14 periods", "100 periods", "1 period", "50 periods"], "answer": "14 periods"},
                {"question": "Can an asset stay overbought during strong trends?", "options": ["Yes, strong trends defy standard RSI thresholds", "No, it must crash instantly", "Weekends only", "Never"], "answer": "Yes, strong trends defy standard RSI thresholds"},
                {"question": "What does RSI measure?", "options": ["Magnitude of recent price changes to evaluate velocity", "Trading volume", "Account balance", "Leverage ratio"], "answer": "Magnitude of recent price changes to evaluate velocity"}
            ]
        },
        "M2 W7: MACD Convergence & Divergence": {
            "concept": "Mastering MACD crossover signals and histogram momentum.",
            "questions": [
                {"question": "What does MACD stand for?", "options": ["Moving Average Convergence Divergence", "Market Asset Cash Distributor", "Margin Asset Calculation Device", "Moving Action Currency Direction"], "answer": "Moving Average Convergence Divergence"},
                {"question": "What generates a bullish MACD crossover signal?", "options": ["MACD line crosses above the signal line", "MACD equals zero", "Volume disappears", "Price drops"], "answer": "MACD line crosses above the signal line"},
                {"question": "What does the MACD histogram measure?", "options": ["The distance between the MACD line and signal line", "Total volume", "Open interest", "Profit"], "answer": "The distance between the MACD line and signal line"},
                {"question": "How is the baseline MACD line calculated?", "options": ["Difference between 12-period EMA and 26-period EMA", "Simple average", "High minus low", "Close divided by open"], "answer": "Difference between 12-period EMA and 26-period EMA"},
                {"question": "What indicates decreasing momentum on the MACD histogram?", "options": ["Bars shrinking toward the zero line", "Bars growing infinitely", "Color constant", "Zero lines moving"], "answer": "Bars shrinking toward the zero line"}
            ]
        },
        "M2 W8: Bollinger Bands & Volatility Squeezes": {
            "concept": "Trading standard deviation breakouts and volatility compression.",
            "questions": [
                {"question": "What do Bollinger Bands consist of?", "options": ["A middle SMA and upper/lower standard deviation bands", "Three resistance lines", "Random indicators", "Volume bars"], "answer": "A middle SMA and upper/lower standard deviation bands"},
                {"question": "What is a Bollinger Band 'Squeeze'?", "options": ["Bands narrowing significantly due to low volatility compression", "Bands expanding", "Account freeze", "Margin call"], "answer": "Bands narrowing significantly due to low volatility compression"},
                {"question": "What usually follows a tight volatility squeeze?", "options": ["An explosive directional breakout move", "Market closure", "Zero volume forever", "Tax payment"], "answer": "An explosive directional breakout move"},
                {"question": "What does it mean when price hugs the upper Bollinger Band?", "options": ["Strong bullish momentum", "Extreme weakness", "Market crash", "Flat range"], "answer": "Strong bullish momentum"},
                {"question": "How are Bollinger Band standard deviations typically set?", "options": ["2 standard deviations from the 20-period SMA", "1 standard deviation", "5 standard deviations", "None"], "answer": "2 standard deviations from the 20-period SMA"}
            ]
        },
        "M3 W9: Position Sizing & Risk Management": {
            "concept": "Protecting capital using the 1% rule and risk-reward ratios.",
            "questions": [
                {"question": "What is the core rule of risk management per trade?", "options": ["Risk only a small fixed percentage (1-2%) of total capital", "Risk 100%", "Never use stops", "Borrow maximum leverage"], "answer": "Risk only a small fixed percentage (1-2%) of total capital"},
                {"question": "How do you calculate position size?", "options": ["Account Risk Dollars divided by Distance to Stop Loss in dollars", "Random guess", "Balance multiplied by 10", "Fee divided by leverage"], "answer": "Account Risk Dollars divided by Distance to Stop Loss in dollars"},
                {"question": "What is Risk-to-Reward Ratio (RRR)?", "options": ["Potential profit target distance compared to potential stop loss risk distance", "Broker fee ratio", "Leverage multiplier", "Win rate percentage"], "answer": "Potential profit target distance compared to potential stop loss risk distance"},
                {"question": "Why is a 1:3 Risk-to-Reward ratio powerful?", "options": ["You can be profitable even with a win rate below 40%", "Guarantees 100% wins", "Eliminates all risk", "Broker bonus"], "answer": "You can be profitable even with a win rate below 40%"},
                {"question": "What is 'ruin risk' in trading?", "options": ["The mathematical probability of losing your entire trading capital", "A minor losing streak", "Tax penalty", "Software glitch"], "answer": "The mathematical probability of losing your entire trading capital"}
            ]
        },
        "M3 W10: Trading Psychology & Emotional Control": {
            "concept": "Overcoming FOMO, revenge trading, and cognitive biases.",
            "questions": [
                {"question": "What is 'Revenge Trading'?", "options": ["Taking impulsive, oversized trades to quickly win back previous losses", "Trading as career", "Closing winning trade", "Following plan"], "answer": "Taking impulsive, oversized trades to quickly win back previous losses"},
                {"question": "What does FOMO stand for in trading?", "options": ["Fear Of Missing Out", "Future Order Market Option", "Fixed Overall Margin", "Fast Online Money"], "answer": "Fear Of Missing Out"},
                {"question": "How do professional traders handle a losing streak?", "options": ["Step away from screens and adhere strictly to risk rules", "Double position size", "Break computer", "Blame market maker"], "answer": "Step away from screens and adhere strictly to risk rules"},
                {"question": "What is confirmation bias?", "options": ["Seeking information confirming your bias while ignoring warning signs", "Trading accurately", "Confirming deposits", "Broker verification"], "answer": "Seeking information confirming your bias while ignoring warning signs"},
                {"question": "Why is keeping emotions detached crucial?", "options": ["Emotions lead to hesitation, breaking rules, and capital destruction", "Emotions increase leverage", "Brokers hate feelings", "Makes trading boring"], "answer": "Emotions lead to hesitation, breaking rules, and capital destruction"}
            ]
        },
        "M3 W11: Trading Journals & Performance Analytics": {
            "concept": "Tracking win rates, risk-reward expectancy, and finding edge through data.",
            "questions": [
                {"question": "Why keep a trading journal?", "options": ["To log mistakes, analyze setup performance, and find your statistical edge", "To show friends", "Tax compliance", "Pass time"], "answer": "To log mistakes, analyze setup performance, and find your statistical edge"},
                {"question": "What is trading Expectancy?", "options": ["Average amount won/lost per dollar risked based on win rate and RRR", "Emotional mood", "Daily goal", "Guaranteed return"], "answer": "Average amount won/lost per dollar risked based on win rate and RRR"},
                {"question": "What metric measures how well you stick to your plan?", "options": ["Plan Adherence Score", "Account balance alone", "Click speed", "Trade count"], "answer": "Plan Adherence Score"},
                {"question": "How often should journal logs be reviewed?", "options": ["Weekly or monthly to detect behavioral leaks and edge decay", "Every 10 years", "Never", "Only after bankruptcy"], "answer": "Weekly or monthly to detect behavioral leaks and edge decay"},
                {"question": "What key data fields should every journal include?", "options": ["Entry price, exit price, stop loss, setup type, emotional state, and screenshots", "Only balance", "Favorite color", "Weather condition"], "answer": "Entry price, exit price, stop loss, setup type, emotional state, and screenshots"}
            ]
        },
        "M3 W12: Building a Master Trading Plan": {
            "concept": "Synthesizing edge, rules, routine, and execution into a master system.",
            "questions": [
                {"question": "What is the purpose of a written Trading Plan?", "options": ["To serve as an objective rulebook removing real-time decision fatigue", "To decorate desk", "To satisfy bank loans", "To predict future"], "answer": "To serve as an objective rulebook removing real-time decision fatigue"},
                {"question": "What should a pre-market routine include?", "options": ["Reviewing macro news, checking key levels, and setting daily risk limits", "Sleeping until noon", "Placing random trades", "Checking social media"
