import streamlit as st
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Trading Duo",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS STYLING (Dark Theme) ---
st.markdown("""
    <style>
    .main {
        background-color: #121212;
    }
    .stButton>button {
        width: 100%;
        background-color: #58cc02;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #46a302;
        color: white;
    }
    .metric-card {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2b2b2b;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- CURRICULUM DATA: FULL MONTH 1 (WEEKS 1 TO 4) ---
LESSONS = [
    # --- WEEK 1: MARKET FUNDAMENTALS & ORDER FLOW ---
    {
        "title": "Week 1, Day 1: Bid, Ask & Spreads",
        "intro": "Welcome to Market Mechanics! In trading, the Bid is what buyers pay, the Ask is what sellers demand, and the difference is the Spread.",
        "questions": [
            {"prompt": "If the Bid price for BTC is $60,000 and the Ask price is $60,010, what is the Spread?", "options": ["$10", "$60,000", "$60,010", "$0"], "answer": "$10"},
            {"prompt": "Which order type executes immediately at the current market price?", "options": ["Limit Order", "Market Order", "Stop-Limit Order", "Good-Til-Canceled"], "answer": "Market Order"},
            {"prompt": "Who typically provides market liquidity by placing resting limit orders?", "options": ["Retail scalpers", "Market Makers", "Exchange server operators", "Tax regulators"], "answer": "Market Makers"}
        ]
    },
    {
        "title": "Week 1, Day 2: Candlestick Anatomy",
        "intro": "Candlesticks show open, high, low, and close prices over a specific timeframe. Green means close > open; Red means close < open.",
        "questions": [
            {"prompt": "What does the 'wick' (shadow) on a candlestick represent?", "options": ["The exact average volume", "The extreme high and low prices reached during the period", "The opening spread cost", "The broker commission fee"], "answer": "The extreme high and low prices reached during the period"},
            {"prompt": "If a candle closes significantly lower than it opened, what color is it typically rendered?", "options": ["Green", "Blue", "Red", "Yellow"], "answer": "Red"},
            {"prompt": "A candlestick with a very small body and long lower wick signaling rejection of lower prices is called a:", "options": ["Marubozu", "Pinbar / Hammer", "Doji grid", "Flat top"], "answer": "Pinbar / Hammer"}
        ]
    },
    {
        "title": "Week 1, Day 3: Risk & Reward Ratios",
        "intro": "Professional trading is risk engineering. Expectancy relies on your Risk-to-Reward Ratio (RRR) and Win Rate.",
        "questions": [
            {"prompt": "If you risk $100 to make $300, what is your Risk-to-Reward Ratio?", "options": ["1:1", "1:2", "1:3", "3:1"], "answer": "1:3"},
            {"prompt": "Why is capital preservation prioritized over high-leverage gambling?", "options": ["To avoid math formulas", "Because consecutive losses can mathematically wipe out an account if position size is too high", "Exchanges ban profitable accounts", "Spreads disappear over time"], "answer": "Because consecutive losses can mathematically wipe out an account if position size is too high"},
            {"prompt": "What metric measures the maximum observed loss from a peak to a trough?", "options": ["Sharpe Ratio", "Drawdown", "Alpha", "Slippage"], "answer": "Drawdown"}
        ]
    },
    {
        "title": "Week 1, Day 4: Python Data Basics",
        "intro": "Automated trading starts with pulling data programmatically. In Python, libraries like pandas handle tabular market history.",
        "questions": [
            {"prompt": "Which Python library is standard for handling tabular data frames in financial backtesting?", "options": ["pandas", "tkinter", "sys", "math"], "answer": "pandas"},
            {"prompt": "What does OHLCV stand for in market datasets?", "options": ["Order, Hedge, Limit, Close, Volume", "Open, High, Low, Close, Volume", "Option, Hold, Leverage, Currency, Value", "Overnight, High, Liquid, Cash, Variable"], "answer": "Open, High, Low, Close, Volume"},
            {"prompt": "Why do scripts use public REST APIs when fetching historical candles?", "options": ["To execute illegal flash loans", "To download past price action history for analysis and backtesting", "To bypass exchange internet fees", "To change exchange server passwords"], "answer": "To download past price action history for analysis and backtesting"}
        ]
    },

    # --- WEEK 2: TECHNICAL INDICATORS & MOMENTUM ---
    {
        "title": "Week 2, Day 1: Volume & RSI Basics",
        "intro": "Volume confirms price trends. The Relative Strength Index (RSI) measures momentum speed and detects overbought/oversold conditions.",
        "questions": [
            {"prompt": "An RSI reading above 70 typically suggests an asset is:", "options": ["Oversold", "Overbought", "Completely illiquid", "Neutral"], "answer": "Overbought"},
            {"prompt": "What does rising price accompanied by declining volume usually warn of?", "options": ["Strong institutional accumulation", "Weakening trend momentum / divergence warning", "Guaranteed market crash", "Zero slippage execution"], "answer": "Weakening trend momentum / divergence warning"},
            {"prompt": "How is RSI standardly bounded mathematically?", "options": ["0 to 100", "-1 to +1", "0 to Infinity", "1 to 10"], "answer": "0 to 100"}
        ]
    },
    {
        "title": "Week 2, Day 2: Volatility & Moving Averages",
        "intro": "Moving averages smooth price action to identify direction. Average True Range (ATR) measures absolute volatility for stop placement.",
        "questions": [
            {"prompt": "Which moving average assigns greater weight to recent price data?", "options": ["Simple Moving Average (SMA)", "Exponential Moving Average (EMA)", "Linear Price Median", "Fixed Constant Average"], "answer": "Exponential Moving Average (EMA)"},
            {"prompt": "If a currency pair's daily ATR is $50, what does that number represent?", "options": ["Its exact closing price tomorrow", "The average price range movement over a specific lookback period", "The broker commission per lot", "The maximum leverage allowed"], "answer": "The average price range movement over a specific lookback period"},
            {"prompt": "What happens when a shorter EMA crosses above a longer EMA?", "options": ["Bearish death cross", "Bullish golden cross / crossover", "Exchange liquidation", "Zero volatility lock"], "answer": "Bullish golden cross / crossover"}
        ]
    },
    {
        "title": "Week 2, Day 3: Bollinger Bands & Squeezes",
        "intro": "Bollinger Bands consist of a middle SMA and outer standard deviation bands. Contractions ('squeezes') precede volatile breakouts.",
        "questions": [
            {"prompt": "What does a Bollinger Band contraction (squeeze) typically indicate?", "options": ["High volatility expansion", "Incoming low volatility period followed by an explosive breakout", "Market closure", "Infinite liquidity"], "answer": "Incoming low volatility period followed by an explosive breakout"},
            {"prompt": "When price touches the upper Bollinger Band consistently during a strong trend, it is known as:", "options": ["Band riding", "Mean reversion bottoming", "Account liquidation", "Spread tightening"], "answer": "Band riding"},
            {"prompt": "What statistical measure sets the width of Bollinger Bands?", "options": ["Standard Deviation", "Fibonacci ratios", "Simple Average variance", "RSI slope"], "answer": "Standard Deviation"}
        ]
    },
    {
        "title": "Week 2, Day 4: Multi-Timeframe Confluence",
        "intro": "Trading with higher timeframe bias increases win probability. Aligning 1-hour trends with 15-minute entries filters noise.",
        "questions": [
            {"prompt": "Why do quantitative traders perform multi-timeframe analysis?", "options": ["To confuse automated bots", "To trade in alignment with dominant institutional momentum", "To increase exchange trading fees", "To eliminate all possible risk"], "answer": "To alignment with dominant institutional momentum"},
            {"prompt": "If the 4H chart shows a strong downtrend, taking long positions on the 1M chart is considered:", "options": ["Trading with the macro trend", "Counter-trend trading (higher risk)", "Arbitrage risk-free", "Grid scaling"], "answer": "Counter-trend trading (higher risk)"},
            {"prompt": "What is a major pitfall of checking lower timeframes too frequently?", "options": ["Over-trading and emotional exhaustion", "Better algorithmic fill rates", "Lower spreads", "Wider profit margins"], "answer": "Over-trading and emotional exhaustion"}
        ]
    },

    # --- WEEK 3: VOLATILITY BREAKOUTS & RANGE TRADING ---
    {
        "title": "Week 3, Day 1: Breakouts vs. Fakeouts",
        "intro": "Breakout trading captures explosive momentum out of consolidation zones. False breakouts (fakeouts) trap aggressive retail traders.",
        "questions": [
            {"prompt": "What is a 'fakeout' in breakout trading?", "options": ["When an exchange halts trading", "When price briefly breaches a support/resistance level before reversing sharply", "When stop loss orders never trigger", "When spreads drop to zero"], "answer": "When price briefly breaches a support/resistance level before reversing sharply"},
            {"prompt": "Which confirmation filter best guards against false breakouts?", "options": ["Waiting for a candle close beyond the level with supporting volume", "Entering blindly the second price touches resistance", "Halving your account leverage", "Switching asset pairs immediately"], "answer": "Waiting for a candle close beyond the level with supporting volume"},
            {"prompt": "What is an Opening Range Breakout (ORB)?", "options": ["Trading the high/low range of the first market session minutes", "Closing all positions at market open", "Arbitrading opening exchange gaps", "Random entry execution"], "answer": "Trading the high/low range of the first market session minutes"}
        ]
    },
    {
        "title": "Week 3, Day 2: Range-Bound Trading",
        "intro": "When markets consolidate horizontally without a clear trend, traders buy at support and sell at resistance (mean reversion).",
        "questions": [
            {"prompt": "In a clear range-bound market, where is the optimal place to take a short position?", "options": ["At the range support floor", "At the range resistance ceiling", "Exactly in the middle of the range", "Whenever volume drops to zero"], "answer": "At the range resistance ceiling"},
            {"prompt": "What tool helps identify overextended price extremes inside a horizontal range?", "options": ["Oscillators like RSI or Stochastic", "Moving average death crosses", "Macro GDP reports", "Exchange funding rates"], "answer": "Oscillators like RSI or Stochastic"},
            {"prompt": "What invalidates a range-bound trading setup?", "options": ["A high-volume breakout and candle close outside the range boundary", "A normal spread expansion", "A minor 5-minute pullback", "Low retail participation"], "answer": "A high-volume breakout and candle close outside the range boundary"}
        ]
    },
    {
        "title": "Week 3, Day 3: Macro Events & Gaps",
        "intro": "High-impact news events (CPI, FOMC, NFP) cause massive volatility spikes, slippage, and price gaps.",
        "questions": [
            {"prompt": "Why do professional risk managers often flatten positions before major FOMC announcements?", "options": ["To avoid extreme slippage and unpredictable wide spreads", "Because exchanges close for maintenance", "To save on electricity bills", "To reset account balances"], "answer": "To avoid extreme slippage and unpredictable wide spreads"},
            {"prompt": "What is an opening market gap?", "options": ["A break in price continuity between the close of one session and open of the next", "An intentional broker error", "A missing order book tier", "Zero volume candle"], "answer": "A break in price continuity between the close of one session and open of the next"},
            {"prompt": "What is slippage?", "options": ["The difference between expected trade execution price and actual fill price", "A technical indicator error", "Broker commission fees", "Leverage liquidation penalty"], "answer": "The difference between expected trade execution price and actual fill price"}
        ]
    },
    {
        "title": "Week 3, Day 4: Quant Performance Metrics",
        "intro": "Systematic traders evaluate strategies using rigorous statistical metrics like Profit Factor, Expectancy, and Maximum Drawdown.",
        "questions": [
            {"prompt": "How is Profit Factor calculated in a backtest report?", "options": ["Gross Profits divided by Gross Losses", "Win Rate minus Loss Rate", "Total Trades times Leverage", "Starting Balance minus Ending Balance"], "answer": "Gross Profits divided by Gross Losses"},
            {"prompt": "What does a positive mathematical trade expectancy mean?", "options": ["Every single trade will be a winner", "Over a large sample size of trades, the system generates positive average returns per dollar risked", "The broker guarantees profits", "Volatility will remain low"], "answer": "Over a large sample size of trades, the system generates positive average returns per dollar risked"},
            {"prompt": "Why is Maximum Drawdown a critical metric for investors?", "options": ["It measures the deepest historical peak-to-trough capital decline", "It predicts exact future market tops", "It calculates exchange server ping speed", "It sets margin call leverage limits"], "answer": "It measures the deepest historical peak-to-trough capital decline"}
        ]
    },

    # --- WEEK 4: SCANNER SETUP & RISK ENGINEERING ---
    {
        "title": "Week 4, Day 1: Automated Push Alerts (ntfy.sh)",
        "intro": "Automated monitoring daemons scan markets 24/7. Integrating lightweight HTTP webhooks like ntfy.sh sends instant mobile push alerts.",
        "questions": [
            {"prompt": "What is the primary benefit of running a background market monitoring script?", "options": ["It eliminates the need to stare at charts all day", "It guarantees 100% profitable trades", "It bypasses exchange trading rules", "It prevents market slippage"], "answer": "It eliminates the need to stare at charts all day"},
            {"prompt": "What protocol do Python scripts use to send HTTP push notifications to services like ntfy.sh?", "options": ["requests library (HTTP POST/GET)", "tkinter canvas rendering", "pandas dataframes", "OS kernel interrupts"], "answer": "requests library (HTTP POST/GET)"},
            {"prompt": "Why is signal filtering essential when building custom alert scanners?", "options": ["To prevent alert fatigue caused by excessive false signals", "To increase exchange trading fees", "To slow down processor speed", "To hide winning trades"], "answer": "To prevent alert fatigue caused by excessive false signals"}
        ]
    },
    {
        "title": "Week 4, Day 2: Position Sizing & Fixed Fractional",
        "intro": "Position sizing controls ruin probability. Fixed fractional risking ensures you risk a strict percentage (e.g. 1%) of your account per trade.",
        "questions": [
            {"prompt": "If your account balance is $10,000 and your risk rule is 1% per trade, what is your maximum dollar loss allowed on a trade?", "options": ["$10", "$100", "$1,000", "$10,000"], "answer": "$100"},
            {"prompt": "How does position sizing change if your stop-loss distance is widened?", "options": ["Position size must be decreased to maintain the same dollar risk", "Position size must be increased", "Risk percentage automatically doubles", "Stop distance has no effect"], "answer": "Position size must be decreased to maintain the same dollar risk"},
            {"prompt": "What is the 'Risk of Ruin'?", "options": ["The mathematical probability of losing 100% of your trading capital", "A minor broker fee", "An RSI divergence signal", "The average daily spread cost"], "answer": "The mathematical probability of losing 100% of your trading capital"}
        ]
    },
    {
        "title": "Week 4, Day 3: Avoiding Overfitting & Curve Fitting",
        "intro": "Backtest optimization can lead to curve fitting—creating a strategy that looks amazing on past data but fails catastrophically live.",
        "questions": [
            {"prompt": "What is 'overfitting' (curve fitting) in algorithmic trading?", "options": ["Adjusting strategy parameters so excessively to past data that it loses predictive power on new data", "Using too many computer monitors", "Trading too many asset pairs", "Running scripts on mobile devices"], "answer": "Adjusting strategy parameters so excessively to past data that it loses predictive power on new data"},
            {"prompt": "What is 'out-of-sample' testing?", "options": ["Testing a strategy on historical data that was NOT used during the optimization phase", "Trading with real money on live exchanges", "Disconnecting your internet router", "Testing code on a different phone model"], "answer": "Testing a strategy on historical data that was NOT used during the optimization phase"},
            {"prompt": "Why do overly complex strategies with 20+ adjustable parameters often fail live?", "options": ["They capture historical noise rather than genuine market mechanics", "Exchanges block complex code", "Python cannot compute them", "Spreads automatically widen"], "answer": "They capture historical noise rather than genuine market mechanics"}
        ]
    },
    {
        "title": "Week 4, Day 4: Month 1 Capstone Review",
        "intro": "You have completed Month 1! You understand market microstructure, indicators, risk math, and Python scanning architecture.",
        "questions": [
            {"prompt": "Which component is most critical for long-term survival in quantitative trading?", "options": ["Strict risk management and capital preservation", "Finding a 100% win-rate indicator", "Using maximum leverage", "Ignoring stop losses"], "answer": "Strict risk management and capital preservation"},
            {"prompt": "What does OHLCV stand for in market data analysis?", "options": ["Open, High, Low, Close, Volume", "Order, Hedge, Limit, Cash, Value", "Overnight, Hold, Liquidity, Chart, Variable", "Option, High, Leverage, Close, Volume"], "answer": "Open, High, Low, Close, Volume"},
            {"prompt": "Ready to advance to Month 2 (Quantitative Scanners & Automated API Execution)?", "options": ["Yes, let's build more algorithms!", "Not yet, review Month 1"], "answer": "Yes, let's build more algorithms!"}
        ]
    }
]

# --- SESSION STATE INITIALIZATION ---
if "hearts" not in st.session_state:
    st.session_state.hearts = 3
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "nav" not in st.session_state:
    st.session_state.nav = "home"
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# --- SIDEBAR METRICS ---
st.sidebar.title("📈 TRADING DUO")
st.sidebar.markdown("---")
st.sidebar.metric(label="❤️ Hearts", value=st.session_state.hearts)
st.sidebar.metric(label="⭐ Total XP", value=st.session_state.xp)

if st.sidebar.button("🏠 Return to Menu"):
    st.session_state.nav = "home"
    st.rerun()

# --- APP ROUTING ---
if st.session_state.nav == "
