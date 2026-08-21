import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TradeX - 3-Month Trading Academy",
    page_icon="📈",
    layout="wide"
)

# --- MONTH 1: Foundations & Market Mechanics ---
lessons_db = {
    "W1L1: Introduction to Financial Markets": {
        "concept": "Understanding how global markets work, asset classes (stocks, crypto, forex, commodities), and supply/demand.",
        "questions": [
            {"question": "What is the primary driver of asset price movement in a free market?", "options": ["Government decree", "Supply and Demand", "Number of employees", "Brokerage fees"], "answer": "Supply and Demand"},
            {"question": "Which asset class represents ownership shares in a corporation?", "options": ["Bonds", "Stocks (Equities)", "Forex", "Commodities"], "answer": "Stocks (Equities)"},
            {"question": "What does 'liquidity' refer to?", "options": ["Ease of converting an asset to cash without moving price", "Water cooling systems in trading servers", "Daily dividend payout rate", "The total debt of a company"], "answer": "Ease of converting an asset to cash without moving price"}
        ]
    },
    "W1L2: Brokers, Exchanges, and Order Routing": {
        "concept": "How orders travel from your platform to the market maker or exchange matching engine.",
        "questions": [
            {"question": "What is a market maker?", "options": ["An artist who draws charts", "An entity that quotes both a buy and a sell price in a financial instrument", "A government regulator", "A retail day trader"], "answer": "An entity that quotes both a buy and a sell price in a financial instrument"},
            {"question": "What is the difference between a market order and a limit order?", "options": ["Market orders execute instantly at current price; limit orders execute only at a specific price or better", "Market orders are illegal", "Limit orders cost more commission", "There is no difference"], "answer": "Market orders execute instantly at current price; limit orders execute only at a specific price or better"},
            {"question": "What does 'bid-ask spread' represent?", "options": ["The broker's physical office space", "The difference between the highest price a buyer is willing to pay and lowest price a seller will accept", "The annual interest rate", "The profit margin of a trade"], "answer": "The difference between the highest price a buyer is willing to pay and lowest price a seller will accept"}
        ]
    },
    "W1L3: Introduction to Leverage and Margin": {
        "concept": "Understanding how borrowing capital from a broker amplifies both potential gains and losses.",
        "questions": [
            {"question": "What does 10x leverage mean?", "options": ["You pay 10x higher commissions", "Your buying power is multiplied by 10", "You can only trade 10 stocks", "Your losses are capped at 10%"], "answer": "Your buying power is multiplied by 10"},
            {"question": "What is a 'margin call'?", "options": ["A telephone call from your broker praising your trades", "A demand by a broker to deposit additional funds when account equity drops below required maintenance", "An order confirmation tone", "An alert when you make a profit"], "answer": "A demand by a broker to deposit additional funds when account equity drops below required maintenance"},
            {"question": "Why does leverage increase risk?", "options": ["It doesn't increase risk", "It magnifies losses at the same rate it magnifies gains", "It locks your money for 10 years", "It doubles exchange fees"], "answer": "It magnifies losses at the same rate it magnifies gains"}
        ]
    },
    "W2L1: Reading Japanese Candlesticks": {
        "concept": "Deconstructing Open, High, Low, and Close (OHLC) data into visual candle bodies and wicks.",
        "questions": [
            {"question": "On a standard green (bullish) candle, what is the bottom of the solid body?", "options": ["The Close", "The Open", "The High", "The absolute low"], "answer": "The Open"},
            {"question": "What do long upper wicks (shadows) indicate?", "options": ["Strong buying pressure", "Selling pressure rejecting higher prices", "Market holiday", "Zero volatility"], "answer": "Selling pressure rejecting higher prices"},
            {"question": "What does a candle with a very small body and long wicks on both sides represent?", "options": ["Strong trend continuation", "Indecision in the market", "Guaranteed market reversal", "Instant liquidation"], "answer": "Indecision in the market"}
        ]
    },
    "W2L2: Basic Market Structure & Trends": {
        "concept": "Identifying higher highs, higher lows, lower highs, and lower lows to map trend direction.",
        "questions": [
            {"question": "What defines a healthy uptrend?", "options": ["Lower highs and lower lows", "Higher highs and higher lows", "Completely flat prices", "Random price swings"], "answer": "Higher highs and higher lows"},
            {"question": "What is a market 'correction' or 'pullback'?", "options": ["A permanent crash", "A temporary counter-trend price movement within a broader prevailing trend", "A correction of broker typos", "The closing bell"], "answer": "A temporary counter-trend price movement within a broader prevailing trend"},
            {"question": "What does a downtrend structure consist of?", "options": ["Higher highs and higher lows", "Lower lows and lower highs", "Sideways consolidation", "Exponential growth"], "answer": "Lower lows and lower highs"}
        ]
    },
    "W2L3: Support and Resistance Levels": {
        "concept": "Mapping historical price boundaries where buying or selling pressure clusters.",
        "questions": [
            {"question": "What is a 'Support' level?", "options": ["A price floor where buying interest overcomes selling pressure", "A price ceiling", "A government financial bailout", "A moving average line"], "answer": "A price floor where buying interest overcomes selling pressure"},
            {"question": "What happens when resistance is broken with high volume?", "options": ["Trading stops", "It frequently flips and acts as future support", "The asset becomes illegal", "Sellers vanish forever"], "answer": "It frequently flips and acts as future support"},
            {"question": "Why are psychological whole numbers effective support/resistance zones?", "options": ["Exchanges highlight them", "Traders naturally cluster orders and stop losses around clean round numbers", "Math laws mandate bounces", "No real significance"], "answer": "Traders naturally cluster orders and stop losses around clean round numbers"}
        ]
    },
    "W3L1: Introduction to Volume Analysis": {
        "concept": "Understanding trading volume as the fuel behind price movements.",
        "questions": [
            {"question": "What does high trading volume during a price breakout indicate?", "options": ["Lack of interest", "Strong market participation and conviction behind the move", "A glitch in the exchange", "Low liquidity"], "answer": "Strong market participation and conviction behind the move"},
            {"question": "What does a price rise on extremely low volume suggest?", "options": ["A powerful sustainable trend", "A weak move that could easily reverse", "Institutional accumulation", "Market certainty"], "answer": "A weak move that could easily reverse"},
            {"question": "Where is volume data typically displayed on a chart?", "options": ["In the top left corner", "As vertical bars at the bottom of the chart", "Inside the RSI window", "In the account balance"], "answer": "As vertical bars at the bottom of the chart"}
        ]
    },
    "W3L2: Timeframes and Multi-Timeframe Analysis": {
        "concept": "Analyzing charts across 1-minute, 1-hour, daily, and weekly intervals to align perspective.",
        "questions": [
            {"question": "Why do traders look at multiple timeframes?", "options": ["To confuse themselves", "To understand the macro trend while timing entries on lower timeframes", "To pay higher subscription fees", "Because brokers require it"], "answer": "To understand the macro trend while timing entries on lower timeframes"},
            {"question": "Which timeframe is generally used for long-term investing outlooks?", "options": ["1-Minute", "5-Second", "Daily or Weekly", "Tick chart"], "answer": "Daily or Weekly"},
            {"question": "What is 'noise' in lower timeframes?", "options": ["Loud computer fans", "Random erratic price fluctuations that lack macro significance", "Audio alerts on trades", "Earnings call recordings"], "answer": "Random erratic price fluctuations that lack macro significance"}
        ]
    },
    "W3L3: Introduction to Chart Patterns": {
        "concept": "Recognizing classic continuation and reversal patterns like triangles and rectangles.",
        "questions": [
            {"question": "What is a consolidation rectangle pattern?", "options": ["A permanent market crash", "A sideways price range between parallel support and resistance lines", "An indicator of infinite profit", "A candlestick anomaly"], "answer": "A sideways price range between parallel support and resistance lines"},
            {"question": "What is an ascending triangle typically considered?", "options": ["A bearish continuation pattern", "A bullish continuation pattern", "A sign of market closure", "A random geometric coincidence"], "answer": "A bullish continuation pattern"},
            {"question": "What does a pattern breakdown mean?", "options": ["The computer screen broke", "Price decisively exits a pattern boundary against the expected direction", "The broker crashed", "All orders are cancelled"], "answer": "Price decisively exits a pattern boundary against the expected direction"}
        ]
    },
    "W4L1: The Psychology of Fear and Greed": {
        "concept": "Mastering emotional discipline and recognizing psychological traps in trading.",
        "questions": [
            {"question": "What is FOMO in trading?", "options": ["Fear Of Missing Out, leading to impulsive chasing of runaway prices", "Financial Order Management Organization", "Fixed Option Market Operation", "Future Over Margin Order"], "answer": "Fear Of Missing Out, leading to impulsive chasing of runaway prices"},
            {"question": "Why do most retail traders lose money?", "options": ["Bad luck", "Lack of emotional control, poor risk management, and revenge trading", "Broker corruption", "Too much education"], "answer": "Lack of emotional control, poor risk management, and revenge trading"},
            {"question": "What is 'revenge trading'?", "options": ["Trading against competitor firms", "Impulsively entering oversized trades immediately after a loss to try and win money back quickly", "Reporting a bad broker", "Shorting a stock you hate"], "answer": "Impulsively entering oversized trades immediately after a loss to try and win money back quickly"}
        ]
    },
    "W4L2: Developing a Trading Plan": {
        "concept": "Creating a rule-based framework for entry, exit, risk, and asset selection.",
        "questions": [
            {"question": "What is the core purpose of a written trading plan?", "options": ["To submit to tax authorities", "To remove emotion by defining objective rules before entering the market", "To guarantee 100% win rates", "To impress friends"], "answer": "To remove emotion by defining objective rules before entering the market"},
            {"question": "Which of these should be included in a trading plan?", "options": ["Entry triggers, stop-loss rules, and profit targets", "Your favorite movie titles", "Daily lunch menu", "Random stock picks from social media"], "answer": "Entry triggers, stop-loss rules, and profit targets"},
            {"question": "When should you evaluate your trading plan?", "options": ["Never", "Regularly in a trading journal during market downtime", "Only when you lose all your money", "Every 10 seconds"], "answer": "Regularly in a trading journal during market downtime"}
        ]
    },
    "W4L3: The Trading Journal & Performance Tracking": {
        "concept": "Logging trades to review mistakes, win rates, and edge over time.",
        "questions": [
            {"question": "What is the primary benefit of maintaining a trading journal?", "options": ["It creates a diary of emotional outbursts", "It tracks data like win rate, average risk-to-reward, and recurring mistakes to improve performance", "It lowers broker fees", "It predicts the next day's high"], "answer": "It tracks data like win rate, average risk-to-reward, and recurring mistakes to improve performance"},
            {"question": "Which metric measures the ratio of gross profits to gross losses?", "options": ["Profit Factor", "Sharpe Ratio", "P/E Ratio", "Dividend Yield"], "answer": "Profit Factor"},
            {"question": "What should you log alongside entry and exit prices?", "options": ["Your emotional state and reasoning for the trade", "Weather conditions", "Laptop battery percentage", "Coffee brand consumed"], "answer": "Your emotional state and reasoning for the trade"}
        ]
    }
}

# --- MONTH 2: Risk Management & Technical Analysis ---
month_2_lessons = {
    "W5L1: Risk-to-Reward Ratio (R:R)": {
        "concept": "Structuring trades so potential rewards significantly outweigh potential risks.",
        "questions": [
            {"question": "What does a 1:3 Risk-to-Reward ratio mean?", "options": ["You risk $3 to make $1", "You risk $1 to make $3", "You lose 3 trades per win", "Broker takes 3% fee"], "answer": "You risk $1 to make $3"},
            {"question": "If you have a 40% win rate with a 1:3 R:R, are you profitable?", "options": ["No, you lose money", "Yes, because your wins outweigh your losses significantly", "You break even exactly", "It's impossible to calculate"], "answer": "Yes, because your wins outweigh your losses significantly"},
            {"question": "Where should your reward target be relative to your risk?", "options": ["Closer than your stop loss", "Further away based on technical levels", "At zero", "Arbitrarily high without reason"], "answer": "Further away based on technical levels"}
        ]
    },
    "W5L2: Stop Loss Placement Strategies": {
        "concept": "Placing stop losses logically behind market structure rather than arbitrary dollar amounts.",
        "questions": [
            {"question": "Where is the best place to put a stop loss for a long trade?", "options": ["Right at your entry price", "Just below a recent key swing low or support level", "At the absolute top of the chart", "Randomly 5 dollars away"], "answer": "Just below a recent key swing low or support level"},
            {"question": "Why is placing a stop loss too tight dangerous?", "options": ["It guarantees profit", "Normal market noise and volatility will trigger it prematurely before the move happens", "Exchanges ban tight stops", "It increases leverage"], "answer": "Normal market noise and volatility will trigger it prematurely before the move happens"},
            {"question": "What is a trailing stop?", "options": ["A stop loss that automatically adjusts upward as price moves in your favor", "A stop loss that moves down when you lose money", "An order that never executes", "A manual broker phone call"], "answer": "A stop loss that automatically adjusts upward as price moves in your favor"}
        ]
    },
    "W5L3: Position Sizing and The 1% Rule": {
        "concept": "Calculating exact share/contract quantities so a single losing trade risks only 1-2% of total capital.",
        "questions": [
            {"question": "What is the golden rule of risk management per individual trade?", "options": ["Risking 100% of capital on high conviction", "Risking no more than 1% to 2% of total capital", "Never using stop losses", "Trading only with borrowed funds"], "answer": "Risking no more than 1% to 2% of total capital"},
            {"question": "If you have a $10,000 account and risk 1%, how much dollar amount are you risking?", "options": ["$10", "$100", "$1,000", "$10,000"], "answer": "$100"},
            {"question": "How does account size affect position sizing?", "options": ["It doesn't matter", "Position size scales up or down to keep dollar risk constant relative to total equity", "Larger accounts mean 50% risk per trade", "Smaller accounts use zero risk"], "answer": "Position size scales up or down to keep dollar risk constant relative to total equity"}
        ]
    },
    "W6L1: Simple Moving Averages (SMA)": {
        "concept": "Smoothing price action over 20, 50, and 200 periods to gauge trend orientation.",
        "questions": [
            {"question": "What does a 200-period Simple Moving Average represent?", "options": ["The exact high of the year", "The average closing price over the last 200 periods, indicating long-term trend", "The number of active traders", "Daily volume total"], "answer": "The average closing price over the last 200 periods, indicating long-term trend"},
            {"question": "What is a 'Golden Cross'?", "options": ["When a short-term MA crosses above a long-term MA (e.g. 50 crossing above 200)", "A religious holiday on Wall Street", "When price drops 50%", "A candlestick pattern"], "answer": "When a short-term MA crosses above a long-term MA (e.g. 50 crossing above 200)"},
            {"question": "How do moving averages behave in ranging (sideways) markets?", "options": ["They give perfectly accurate signals", "They flatten out and can generate false crossover signals", "They disappear", "They point straight up"], "answer": "They flatten out and can generate false crossover signals"}
        ]
    },
    "W6L2: Exponential Moving Averages (EMA)": {
        "concept": "Giving more weight to recent price data to react faster to trend shifts.",
        "questions": [
            {"question": "What is the main difference between SMA and EMA?", "options": ["EMA gives more weight to recent prices, making it more responsive", "SMA is only used for crypto", "EMA has no mathematical formula", "There is no difference"], "answer": "EMA gives more weight to recent prices, making it more responsive"},
            {"question": "Which EMA lengths are popular among day traders?", "options": ["9, 21, and 50", "1,000 and 5,000", "3 and 7 only", "None"], "answer": "9, 21, and 50"},
            {"question": "What does price holding above a rising 21 EMA indicate?", "options": ["Strong short-term bullish momentum", "Imminent bankruptcy", "Market closure", "Zero volatility"], "answer": "Strong short-term bullish momentum"}
        ]
    },
    "W6L3: Relative Strength Index (RSI)": {
        "concept": "Measuring velocity of price changes to identify overbought and oversold extremes.",
        "questions": [
            {"question": "What range does the RSI oscillator operate within?", "options": ["0 to 100", "-1 to +1", "0 to infinity", "50 to 500"], "answer": "0 to 100"},
            {"question": "An RSI reading above 70 typically indicates:", "options": ["Oversold conditions", "Overbought conditions, suggesting potential pullback", "Zero momentum", "Exact fair value"], "answer": "Overbought conditions, suggesting potential pullback"},
            {"question": "What is RSI divergence?", "options": ["When RSI and price move in opposite directions, signaling potential reversal", "When RSI equals 50", "A broker error", "High trading volume"], "answer": "When RSI and price move in opposite directions, signaling potential reversal"}
        ]
    },
    "W7L1: MACD (Moving Average Convergence Divergence)": {
        "concept": "Tracking momentum and trend changes using relationship between two exponential moving averages.",
        "questions": [
            {"question": "What components make up the MACD indicator?", "options": ["MACD line, Signal line, and Histogram", "Support, resistance, and volume", "Open, high, low, close", "Bid and ask spread"], "answer": "MACD line, Signal line, and Histogram"},
            {"question": "When does a bullish MACD crossover occur?", "options": ["When the MACD line crosses below the signal line", "When the MACD line crosses above the signal line", "When histogram hits zero", "When volume disappears"], "answer": "When the MACD line crosses above the signal line"},
            {"question": "What does the MACD histogram measure?", "options": ["The distance between the MACD line and the signal line", "Total daily exchange volume", "Account leverage", "Profit and loss"], "answer": "The distance between the MACD line and the signal line"}
        ]
    }
}  # <--- Make sure this closing brace is present!
