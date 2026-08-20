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
    # Gamification Stats Bar
    st.markdown(f"""
        <div class="duo-stats">
            <span>🔥 Streak: {st.session_state.streak} Days</span>
            <span>⚡ XP: {st.session_state.xp}</span>
            <span>❤️ Hearts: {'❤️' * st.session_state.hearts}</span>
        </div>
    """, unsafe_allow_html=True)

    # Modularized Curriculum Databases to prevent syntax parsing errors
    month1_lessons = {
        "Month 1, Week 1: Market Mechanics & Orders": {
            "concept": "Mastering order types (Market, Limit, Stop), liquidity providers, and exchange execution mechanics.",
            "questions": [
                {"question": "What is the primary role of a Market Maker?", "options": ["To crash the price", "To provide liquidity and facilitate trades", "To charge high trading taxes", "To print money"], "answer": "To provide liquidity and facilitate trades"},
                {"question": "What term describes the price difference between what buyers pay and sellers accept?", "options": ["Leverage Ratio", "Bid-Ask Spread", "Dividend Yield", "Slippage Fee"], "answer": "Bid-Ask Spread"},
                {"question": "Which order guarantees execution speed but not a specific price?", "options": ["Limit Order", "Market Order", "Stop-Loss Order", "GTC Order"], "answer": "Market Order"},
                {"question": "What is a Limit Order used for?", "options": ["Buying instantly at any price", "Specifying an exact price to buy or sell", "Closing an account", "Avoiding broker fees"], "answer": "Specifying an exact price to buy or sell"},
                {"question": "What happens to spreads during high volatility events?", "options": ["They tighten to zero", "They widen significantly", "They disappear entirely", "The exchange pauses forever"], "answer": "They widen significantly"}
            ]
        },
        "Month 1, Week 2: Support & Resistance Zones": {
            "concept": "Identifying structural turning points where buyers or sellers historically dominate price action.",
            "questions": [
                {"question": "When price hits a 'Resistance' level, what usually happens?", "options": ["Sellers step in and push price down", "Buyers panic and buy everything", "The exchange shuts down", "Nothing changes"], "answer": "Sellers step in and push price down"},
                {"question": "How is a 'Support' level viewed in technical analysis?", "options": ["A price ceiling", "A price floor where buying interest is strong", "A guaranteed loss point", "An indicator of bankruptcy"], "answer": "A price floor where buying interest is strong"},
                {"question": "What often happens when a major resistance level is broken with high volume?", "options": ["It flips into a new support level", "The asset gets delisted", "Trading is suspended", "Volume drops to zero"], "answer": "It flips into a new support level"},
                {"question": "Why do round psychological numbers act as barriers?", "options": ["Algorithms ignore them", "Many human traders cluster orders there", "Government rules mandate it", "They have zero volume"], "answer": "Many human traders cluster orders there"},
                {"question": "What is a 'false breakout'?", "options": ["Broker theft", "Price briefly spiking past a level to trigger stops before reversing", "Permanent market crash", "Screen glitch"], "answer": "Price briefly spiking past a level to trigger stops before reversing"}
            ]
        },
        "Month 1, Week 3: Candlestick Pattern Recognition": {
            "concept": "Decoding single and multi-candle formations like Hammers, Engulfing patterns, and Dojis.",
            "questions": [
                {"question": "What does a long lower wick on a Hammer candle tell you?", "options": ["Extreme selling panic", "Price rejection and buyer defense", "Market closure", "Zero volume"], "answer": "Price rejection and buyer defense"},
                {"question": "What kind of body size is characteristic of a classic Hammer candle?", "options": ["Massive body", "Small body near the upper end of the range", "No body", "Square body"], "answer": "Small body near the upper end of the range"},
                {"question": "Where do you look for a Hammer pattern for a bullish reversal?", "options": ["At the top of a bull run", "At the bottom of a downtrend near support", "In a flat range", "On a 5-second chart"], "answer": "At the bottom of a downtrend near support"},
                {"question": "What does a Bullish Engulfing pattern indicate?", "options": ["Sellers taking total control", "Buyers completely overwhelming previous selling momentum", "Market consolidation", "Low liquidity"], "answer": "Buyers completely overwhelming previous selling momentum"},
                {"question": "What does a Doji candlestick represent?", "options": ["Strong buyer momentum", "Strong seller momentum", "Indecision between buyers and sellers", "Exchange shutdown"], "answer": "Indecision between buyers and sellers"}
            ]
        },
        "Month 1, Week 4: Trend Structure & Momentum": {
            "concept": "Mapping Higher Highs, Higher Lows, Lower Highs, and identifying market phase cycles.",
            "questions": [
                {"question": "What defines a healthy Bull Market structure?", "options": ["Lower highs and lower lows", "Higher highs and higher lows", "Flat sideways chopping", "Constant crashes"], "answer": "Higher highs and higher lows"},
                {"question": "What defines a Bear Market structure?", "options": ["Higher highs", "Lower highs and lower lows", "Rapid accumulation", "Zero volatility"], "answer": "Lower highs and lower lows"},
                {"question": "What is market consolidation?", "options": ["A sharp parabolic pump", "A sideways trading range indicating indecision or accumulation", "A permanent market close", "A margin call event"], "answer": "A sideways trading range indicating indecision or accumulation"},
                {"question": "How do you identify a trend reversal?", "options": ["When structure breaks (e.g., a downtrend makes a higher high)", "When volume drops to zero", "When you feel like trading", "When news stations report on it"], "answer": "When structure breaks (e.g., a downtrend makes a higher high)"},
                {"question": "What timeframes should trend analysis be checked on?", "options": ["Only 1-minute charts", "Multi-timeframe analysis (e.g., Daily, 4H, 1H)", "Only yearly charts", "Timeframes do not matter"], "answer": "Multi-timeframe analysis (e.g., Daily, 4H, 1H)"}
            ]
        }
    }

    month2_lessons = {
        "Month 2, Week 5: Moving Averages & Trend Filters": {
            "concept": "Utilizing Simple and Exponential Moving Averages (SMA/EMA) alongside Golden and Death crosses.",
            "questions": [
                {"question": "What is the key difference between SMA and EMA?", "options": ["EMA gives more weight to recent prices", "SMA is only used for crypto", "EMA lags further behind price", "There is no difference"], "answer": "EMA gives more weight to recent prices"},
                {"question": "What is a 'Golden Cross'?", "options": ["When a short-term MA crosses above a long-term MA", "When price drops 50%", "A tax rule", "A candlestick pattern"], "answer": "When a short-term MA crosses above a long-term MA"},
                {"question": "What does a 'Death Cross' signify?", "options": ["Bullish continuation", "Bearish momentum when a short MA crosses below a long MA", "Broker bankruptcy", "High volume breakout"], "answer": "Bearish momentum when a short MA crosses below a long MA"},
                {"question": "How do traders use MAs dynamically?", "options": ["As dynamic support and resistance levels", "To predict exact future prices down to the cent", "To calculate taxes", "To place stop losses blindly"], "answer": "As dynamic support and resistance levels"},
                {"question": "What is a common pitfall of moving averages in choppy markets?", "options": ["They provide too many false whipsaw signals", "They stop working entirely", "They delete data", "They increase broker fees"], "answer": "They provide too many false whipsaw signals"}
            ]
        },
        "Month 2, Week 6: Oscillators & RSI Divergence": {
            "concept": "Measuring market momentum using the Relative Strength Index (RSI) and spotting hidden divergences.",
            "questions": [
                {"question": "What does an RSI reading above 70 typically indicate?", "options": ["Oversold conditions", "Overbought conditions", "Zero momentum", "Market closure"], "answer": "Overbought conditions"},
                {"question": "What does an RSI reading below 30 typically suggest?", "options": ["Overbought conditions", "Oversold conditions", "Guaranteed profit", "Maximum leverage"], "answer": "Oversold conditions"},
                {"question": "What is a bullish RSI divergence?", "options": ["Price makes lower lows while RSI makes higher lows", "Price and RSI both crash", "RSI stays at 50", "Price goes straight up"], "answer": "Price makes lower lows while RSI makes higher lows"},
                {"question": "What does momentum divergence signal to a trader?", "options": ["A potential weakening of the current trend", "Immediate exchange shutdown", "Infinite profits", "Nothing of importance"], "answer": "A potential weakening of the current trend"},
                {"question": "Can RSI stay in overbought/oversold territory during strong trends?", "options": ["No, it reverses instantly", "Yes, strong trends can keep RSI extended", "Only on weekends", "Only in stocks"], "answer": "Yes, strong trends can keep RSI extended"}
            ]
        },
        "Month 2, Week 7: Risk Management & Position Sizing": {
            "concept": "Preserving capital with stop losses, risk-to-reward ratios (1:2, 1:3), and the 1-2% rule.",
            "questions": [
                {"question": "Why is capital preservation the #1 rule of trading?", "options": ["To avoid taxes", "Because you cannot trade without capital", "To impress friends", "Brokers require it"], "answer": "Because you cannot trade without capital"},
                {"question": "What is the recommended maximum percentage of account capital to risk on a single trade?", "options": ["50%", "1% to 2%", "100%", "0.001%"], "answer": "1% to 2%"},
                {"question": "What is a Risk-to-Reward ratio of 1:3?", "options": ["Risking $100 to make $300", "Risking $300 to make $100", "Losing everything", "A guaranteed win"], "answer": "Risking $100 to make $300"},
                {"question": "Where should a standard stop loss be placed?", "options": ["Randomly", "Just beyond invalidation points like key support/resistance", "At your profit target", "Never use stop losses"], "answer": "Just beyond invalidation points like key support/resistance"},
                {"question": "How does math impact drawdowns?", "options": ["A 50% loss requires a 100% gain to recover", "Losses do not matter", "Gains compound instantly", "Math does not apply to trading"], "answer": "A 50% loss requires a 100% gain to recover"}
            ]
        },
        "Month 2, Week 8: Volume & Volatility Analysis": {
            "concept": "Analyzing Volume Profiles, Bollinger Bands, and Average True Range (ATR) to gauge market force.",
            "questions": [
                {"question": "What does high volume on a breakout confirm?", "options": ["Strong participation and valid move", "A fake move", "Low liquidity", "Market manipulation"], "answer": "Strong participation and valid move"},
                {"question": "What do Bollinger Bands expanding indicate?", "options": ["Decreasing volatility", "Increasing market volatility", "Market close", "Fixed pricing"], "answer": "Increasing market volatility"},
                {"question": "What is a 'Bollinger Band Squeeze'?", "options": ["A period of low volatility often preceding a major breakout", "A broker penalty", "A forced liquidation", "An indicator error"], "answer": "A period of low volatility often preceding a major breakout"},
                {"question": "What is Average True Range (ATR) used for?", "options": ["Measuring market volatility to set stop losses", "Predicting exact tops", "Calculating dividends", "Tracking news events"], "answer": "Measuring market volatility to set stop losses"},
                {"question": "What does low volume during an upward price push suggest?", "options": ["Weak buying interest and potential trap", "Massive institutional buying", "Guaranteed continuation", "Maximum safety"], "answer": "Weak buying interest and potential trap"}
            ]
        }
    }

    month3_lessons = {
        "Month 3, Week 9: Trading Psychology & Emotional Control": {
            "concept": "Conquering FOMO, greed, panic, and revenge trading (tilt) through strict discipline.",
            "questions": [
                {"question": "What does FOMO stand for?", "options": ["Fear Of Missing Out", "Financial Order Management Organization", "Future Options Market Order", "Forex Margin Out"], "answer": "Fear Of Missing Out"},
                {"question": "What is 'Revenge Trading'?", "options": ["A profitable strategy", "Trading impulsively to recover losses immediately after a bad trade", "Reporting a bad broker", "Hedging a portfolio"], "answer": "Trading impulsively to recover losses immediately after a bad trade"},
                {"question": "Why is emotional detachment vital for traders?", "options": ["Emotions lead to impulsive, irrational decision-making", "Trading requires robots", "Feelings increase fees", "It doesn't matter"], "answer": "Emotions lead to impulsive, irrational decision-making"},
                {"question": "What should you do after experiencing consecutive losses ('tilt')?", "options": ["Double your position size", "Step away from the screens and clear your head", "Avenge the loss immediately", "Close your bank account"], "answer": "Step away from the screens and clear your head"},
                {"question": "How does discipline trump strategy?", "options": ["A great strategy fails without disciplined execution", "Discipline replaces analysis", "Strategy is useless", "It doesn't"], "answer": "A great strategy fails without disciplined execution"}
            ]
        },
        "Month 3, Week 10: Macroeconomics & Fundamental Drivers": {
            "concept": "Understanding interest rates, inflation data (CPI), central bank policies, and global catalysts.",
            "questions": [
                {"question": "How do rising interest rates typically impact risk assets like tech stocks and crypto?", "options": ["They cause massive rallies", "They generally reduce liquidity and pressure risk assets downward", "They have zero impact", "They eliminate inflation"], "answer": "They generally reduce liquidity and pressure risk assets downward"},
                {"question": "What does CPI (Consumer Price Index) measure?", "options": ["Inflation and changes in purchasing power", "Stock market volume", "Cryptocurrency mining difficulty", "Broker commissions"], "answer": "Inflation and changes in purchasing power"},
                {"question": "What is a 'Hawkish' central bank stance?", "options": ["Favoring high interest rates to combat inflation", "Printing infinite money", "Lowering rates to zero", "Ignoring the economy"], "answer": "Favoring high interest rates to combat inflation"},
                {"question": "Why do traders watch employment reports (like Non-Farm Payrolls)?", "options": ["To gauge overall economic health and Fed policy shifts", "To check weather conditions", "To find holiday schedules", "For fun"], "answer": "To gauge overall economic health and Fed policy shifts"},
                {"question": "What is 'priced in' market behavior?", "options": ["When expected news is already reflected in current asset prices", "Free shipping", "Guaranteed profits", "Broker error"], "answer": "When expected news is already reflected in current asset prices"}
            ]
        },
        "Month 3, Week 11: Trading Journals & Performance Analytics": {
            "concept": "Tracking win rates, risk-reward expectancy, and finding edge through rigorous data logging.",
            "questions": [
                {"question": "Why do professional traders keep a trading journal?", "options": ["To log mistakes, t
