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

    # Expanded Month 1 (Day-by-Day with 5 Questions each) + Month 2 & 3 Frameworks
    lessons_db = {
        # --- MONTH 1, WEEK 1: Market Mechanics & Orders ---
        "M1 W1 D1: Bid-Ask Spreads & Liquidity": {
            "concept": "Understanding order books, market makers, and how liquidity works.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["Crash price", "Provide liquidity", "Charge high taxes", "Print money"], "answer": "Provide liquidity"},
                {"question": "What term describes the price gap between buyers and sellers?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "What happens to spreads during high volatility?", "options": ["They tighten", "They widen significantly", "They disappear", "Exchanges pause"], "answer": "They widen significantly"},
                {"question": "Who absorbs market orders on an exchange?", "options": ["Limit orders sitting in the order book", "The government", "Miners", "Random generators"], "answer": "Limit orders sitting in the order book"},
                {"question": "What is market depth?", "options": ["The ocean depth", "The volume of pending buy and sell orders at various prices", "Account balance", "Leverage limit"], "answer": "The volume of pending buy and sell orders at various prices"}
            ]
        },
        "M1 W1 D2: Market vs Limit Orders": {
            "concept": "Executing trades with execution speed vs price precision.",
            "questions": [
                {"question": "Which order guarantees speed over price execution?", "options": ["Limit Order", "Market Order", "Stop-Loss", "GTC Order"], "answer": "Market Order"},
                {"question": "What is a Limit Order used for?", "options": ["Buying instantly at any price", "Specifying an exact target price to execute", "Closing account", "Avoiding taxes"], "answer": "Specifying an exact target price to execute"},
                {"question": "What is slippage?", "options": ["Ice on a chart", "The difference between expected price and execution price", "Broker bonus", "Platform crash"], "answer": "The difference between expected price and execution price"},
                {"question": "When should you prefer a Limit Order?", "options": ["During low liquidity or to avoid high slippage", "During a panic crash", "Never", "When trading with 100x leverage"], "answer": "During low liquidity or to avoid high slippage"},
                {"question": "What does IOC (Immediate-Or-Cancel) mean?", "options": ["Cancel account", "Execute immediately or cancel unfulfilled parts", "Ignore order conditions", "Infinite order creation"], "answer": "Execute immediately or cancel unfulfilled parts"}
            ]
        },
        "M1 W1 D3: Stop Orders & Trigger Mechanics": {
            "concept": "Using conditional trigger orders to manage breakouts and risk.",
            "questions": [
                {"question": "What triggers a Stop-Loss order?", "options": ["Price reaching a specified trigger price", "Broker manual click", "Random timer", "Volume dropping"], "answer": "Price reaching a specified trigger price"},
                {"question": "What is a Stop-Limit order?", "options": ["An order that turns into a limit order once triggered", "A permanent ban", "A free trade", "A market order"], "answer": "An order that turns into a limit order once triggered"},
                {"question": "Why use a Stop-Loss?", "options": ["To limit potential trading losses automatically", "To guarantee profit", "To increase fees", "To double margin"], "answer": "To limit potential trading losses automatically"},
                {"question": "Can a Stop-Limit order fail to execute?", "options": ["No, never", "Yes, if price moves past the limit price too fast", "Only on weekends", "Only in crypto"], "answer": "Yes, if price moves past the limit price too fast"},
                {"question": "What is a Trailing Stop?", "options": ["A stop loss that automatically tracks favorable price movement", "A lagging indicator", "A fixed price floor", "A market exit strategy"], "answer": "A stop loss that automatically tracks favorable price movement"}
            ]
        },
        "M1 W1 D4: Margin & Leverage Basics": {
            "concept": "Amplifying exposure using borrowed capital responsibly.",
            "questions": [
                {"question": "What is leverage in trading?", "options": ["Borrowing funds from a broker to increase position size", "A physical tool", "A tax penalty", "A type of chart"], "answer": "Borrowing funds from a broker to increase position size"},
                {"question": "What is a Margin Call?", "options": ["A phone call from your mom", "A demand to add funds when losses approach your collateral limit", "Winning a prize", "Closing a winning trade"], "answer": "A demand to add funds when losses approach your collateral limit"},
                {"question": "What happens with 10x leverage if the market moves 10% against you?", "options": ["You break even", "You lose your entire margin collateral (liquidation)", "You double money", "Nothing"], "answer": "You lose your entire margin collateral (liquidation)"},
                {"question": "What is initial margin?", "options": ["Collateral required to open a leveraged position", "Free money", "Broker fee", "Profit target"], "answer": "Collateral required to open a leveraged position"},
                {"question": "Is high leverage recommended for beginners?", "options": ["Yes, always", "No, it rapidly destroys accounts", "Only on Fridays", "Only for stocks"], "answer": "No, it rapidly destroys accounts"}
            ]
        },
        "M1 W1 D5: Settlement & Exchange Architecture": {
            "concept": "Understanding centralized vs decentralized exchanges and settlement cycles.",
            "questions": [
                {"question": "What is a CEX (Centralized Exchange)?", "options": ["A platform managed by a company matching orders", "A peer-to-peer network", "A bank vault", "A chart pattern"], "answer": "A platform managed by a company matching orders"},
                {"question": "What is a DEX (Decentralized Exchange)?", "options": ["An exchange running via smart contracts on a blockchain", "A physical trading floor", "A closed database", "A stock broker"], "answer": "An exchange running via smart contracts on a blockchain"},
                {"question": "What does T+1 settlement mean?", "options": ["Trades settle one business day after execution", "Trades take 1 year", "Instant cash out", "Zero settlement"], "answer": "Trades settle one business day after execution"},
                {"question": "What is counterparty risk?", "options": ["The risk that the other party or exchange fails to fulfill obligations", "Market volatility", "Slippage risk", "Spread cost"], "answer": "The risk that the other party or exchange fails to fulfill obligations"},
                {"question": "What is cold storage?", "options": ["A refrigerator", "Offline digital wallet security for keeping assets safe from hacks", "A trading strategy", "A market downturn"], "answer": "Offline digital wallet security for keeping assets safe from hacks"}
            ]
        },

        # --- MONTH 1, WEEK 2: Support & Resistance Zones ---
        "M1 W2 D1: Identifying Support Floors": {
            "concept": "Finding historical price levels where buying pressure overcomes selling pressure.",
            "questions": [
                {"question": "What is a Support level?", "options": ["A price ceiling", "A price floor where buyers historically step in", "A guaranteed profit point", "A tax bracket"], "answer": "A price floor where buyers historically step in"},
                {"question": "Why do support zones work?", "options": ["Because human traders and algorithms remember historical reaction points", "Magic", "Government mandates", "Random chance"], "answer": "Because human traders and algorithms remember historical reaction points"},
                {"question": "How many touches make a valid support level more reliable?", "options": ["1 touch", "Multiple touches over time", "Zero touches", "1000 touches"], "answer": "Multiple touches over time"},
                {"question": "What happens when price breaks below strong support?", "options": ["It usually accelerates downward", "It bounces to infinity", "Trading stops", "Nothing"], "answer": "It usually accelerates downward"},
                {"question": "Where should stop losses be placed relative to support?", "options": ["Right on the line", "Just below the support zone invalidation point", "At the top", "Never use them"], "answer": "Just below the support zone invalidation point"}
            ]
        },
        "M1 W2 D2: Identifying Resistance Ceilings": {
            "concept": "Locating structural barriers where selling pressure halts upward momentum.",
            "questions": [
                {"question": "What happens when price approaches Resistance?", "options": ["Sellers step in and push price down", "Buyers panic buy", "Volume disappears", "Exchanges close"], "answer": "Sellers step in and push price down"},
                {"question": "What forms a resistance ceiling?", "options": ["Previous swing highs where profit-taking occurred", "Moving averages only", "Random lines", "Exchange fees"], "answer": "Previous swing highs where profit-taking occurred"},
                {"question": "What indicates a weak resistance level?", "options": ["High volume rejection", "A quick touch with low volume that easily punches through", "10 years of history", "Major news"], "answer": "A quick touch with low volume that easily punches through"},
                {"question": "How do short sellers use resistance?", "options": ["To enter short positions with tight stop-losses above the ceiling", "To buy long", "To ignore the market", "To calculate taxes"], "answer": "To enter short positions with tight stop-losses above the ceiling"},
                {"question": "What is a double top pattern?", "options": ["Two peaks near the same resistance level signaling potential reversal", "A bullish continuation", "An indicator error", "High leverage"], "answer": "Two peaks near the same resistance level signaling potential reversal"}
            ]
        },
        "M1 W2 D3: Polarity Swaps (Support Becomes Resistance)": {
            "concept": "Mastering structural flips when broken levels switch roles.",
            "questions": [
                {"question": "What is a polarity swap?", "options": ["When broken support turns into new resistance (or vice versa)", "A broker glitch", "A tax swap", "A leverage flip"], "answer": "When broken support turns into new resistance (or vice versa)"},
                {"question": "Why does a polarity swap occur?", "options": ["Traders who bought at support are now trapped and want to exit at breakeven", "Random chance", "Exchange rules", "Algorithm updates"], "answer": "Traders who bought at support are now trapped and want to exit at breakeven"},
                {"question": "How do breakout traders trade a polarity swap?", "options": ["Wait for a retest of the broken level to enter in the direction of the breakout", "Sell immediately", "Close account", "Ignore it"], "answer": "Wait for a retest of the broken level to enter in the direction of the breakout"},
                {"question": "What confirms a successful polarity flip retest?", "options": ["A rejection candle forming on low volume retest", "High volume crash", "Immediate liquidation", "Market closure"], "answer": "A rejection candle forming on low volume retest"},
                {"question": "What is a failed polarity flip called?", "options": ["A fakeout or false breakout", "A golden cross", "A margin call", "A dividend"], "answer": "A fakeout or false breakout"}
            ]
        },
        "M1 W2 D4: Psychological Round Numbers": {
            "concept": "Recognizing how human behavior impacts round integer pricing barriers.",
            "questions": [
                {"question": "Why do round numbers (e.g., $100, $50,000) act as barriers?", "options": ["Human psychological clustering of orders", "Code constraints", "Government limits", "Zero volume"], "answer": "Human psychological clustering of orders"},
                {"question": "Where do retail limit orders often cluster?", "options": ["At exact round numbers", "Random decimals", "Nowhere", "Only negative numbers"], "answer": "At exact round numbers"},
                {"question": "What is 'front-running' a round number?", "options": ["Placing orders slightly ahead of a psychological barrier", "Running fast", "Broker theft", "Illegal mining"], "answer": "Placing orders slightly ahead of a psychological barrier"},
                {"question": "What happens after a major round number is decisively broken?", "options": ["Rapid momentum toward the next round target", "Market shutdown", "Zero volatility", "Permanent freeze"], "answer": "Rapid momentum toward the next round target"},
                {"question": "Do institutional algorithms look at round numbers?", "options": ["Yes, they target liquidity pools clustered around them", "No, they ignore numbers", "Only on weekends", "Only in forex"], "answer": "Yes, they target liquidity pools clustered around them"}
            ]
        },
        "M1 W2 D5: Trendlines & Dynamic Channels": {
            "concept": "Drawing diagonal support and resistance slopes.",
            "questions": [
                {"question": "How many swing points are required to draw a valid trendline?", "options": ["At least 2 points, with a 3rd point confirming validation", "1 point", "100 points", "Zero points"], "answer": "At least 2 points, with a 3rd point confirming validation"},
                {"question": "What does an ascending trendline represent?", "options": ["Rising support where buyers step in higher each time", "A bear market", "Flat range", "A crash"], "answer": "Rising support where buyers step in higher each time"},
                {"question": "What is a parallel price channel?", "options": ["Support and resistance trendlines running parallel to contain price action", "An indicator error", "A broker fee", "A margin limit"], "answer": "Support and resistance trendlines running parallel to contain price action"},
                {"question": "How do traders use channel boundaries?", "options": ["Buy near channel support, take profit near channel resistance", "Ignore them", "Sell everything", "Use 100x leverage"], "answer": "Buy near channel support, take profit near channel resistance"},
                {"question": "What does a trendline break signal?", "options": ["Potential trend exhaustion or reversal", "Guaranteed profit", "Exchange update", "System glitch"], "answer": "Potential trend exhaustion or reversal"}
            ]
        },

        # --- MONTH 1, WEEK 3: Candlestick Pattern Recognition ---
        "M1 W3 D1: Single Candlestick Rejections (Hammers & Shooting Stars)": {
            "concept": "Decoding wicks and body structures for immediate reversal signals.",
            "questions": [
                {"question": "What does a long lower wick on a Hammer indicate?", "options": ["Price rejection and aggressive buyer defense at lows", "Extreme selling", "Market closure", "Zero volume"], "answer": "Price rejection and aggressive buyer defense at lows"},
                {"question": "Where should a valid Hammer appear for a bullish setup?", "options": ["At the bottom of a downtrend near support", "At the top of a bull run", "In a flat chop", "On a 1-second chart"], "answer": "At the bottom of a downtrend near support"},
                {"question": "What is a Shooting Star candle?", "options": ["A bearish reversal candle with a long upper wick at resistance", "A bullish breakout", "A moving average", "A volume spike"], "answer": "A bearish reversal candle with a long upper wick at resistance"},
                {"question": "What does the body size of a classic hammer look 
