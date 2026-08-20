import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TradeX - Dashboard & Academy",
    page_icon="📈",
    layout="wide"
)

# Custom Styling for TradeX Dark Mode Theme
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
    .lesson-item {
        background-color: #161a25;
        border: 1px solid #2a2e39;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .watchlist-item {
        background: #1e222d;
        padding: 12px 15px;
        border-radius: 8px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        border: 1px solid #2a2e39;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## TRADE<span style='color: #2962ff;'>X</span>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (Learn)", "Markets", "Paper Trading"])

if page == "Dashboard":
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>WELCOME BACK</p>", unsafe_allow_html=True)
    st.title("Trading Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px; font-size: 0.9rem;">Portfolio Value</p>
            <h2 style="margin: 0; color: #ffffff;">$10,000.00</h2>
            <span style="color: #089981; font-weight: bold; font-size: 0.85rem;">+2.45%</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px; font-size: 0.9rem;">Today's Profit</p>
            <h2 style="margin: 0; color: #ffffff;">$245.60</h2>
            <span style="color: #089981; font-weight: bold; font-size: 0.85rem;">+2.45%</span>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px; font-size: 0.9rem;">Available Cash</p>
            <h2 style="margin: 0; color: #ffffff;">$8,750.00</h2>
            <span style="color: #848e9c; font-size: 0.85rem;">Ready to trade</span>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    chart_col, watch_col = st.columns([3, 1])
    with chart_col:
        st.markdown("### BTC / USD")
        st.markdown("## $68,420.50")
        
        cols = st.columns([1, 1, 1, 1, 6])
        with cols[0]: st.button("1H")
        with cols[1]: st.button("1D", type="primary")
        with cols[2]: st.button("1W")
        with cols[3]: st.button("1M")
        
        chart_data = pd.DataFrame(
            np.random.randn(50, 1).cumsum() + 68420,
            columns=["Price"]
        )
        st.line_chart(chart_data, color="#2962ff", height=350)
        
    with watch_col:
        st.markdown("### Watchlist")
        watchlist_items = {"BTC": "$68,420", "ETH": "$3,420", "AAPL": "$227.10", "TSLA": "$341.20"}
        for asset, price in watchlist_items.items():
            st.markdown(f"""
            <div class="watchlist-item">
                <b>{asset}</b>
                <span style="color: #848e9c;">{price}</span>
            </div>
            """, unsafe_allow_html=True)

elif page == "Trading Academy (Learn)":
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>LEARN</p>", unsafe_allow_html=True)
    st.title("7-Day Masterclass Curriculum")
    st.write("Explore our comprehensive program: 7 Days, 5 Sessions per Day, and 4 Lessons per Session (140 Total Lessons).")
    
    # Comprehensive 7-Day Curriculum Structure
    curriculum = {
        "Day 1: Market Foundations & Mechanics": {
            "Session 1: Introduction to Exchanges": [
                "1.1 What is a Financial Exchange?", 
                "1.2 Market Makers vs. Market Takers", 
                "1.3 The Mechanics of the Bid-Ask Spread", 
                "1.4 Understanding Market vs. Limit Orders"
            ],
            "Session 2: Core Asset Classes": [
                "2.1 Equities and Stock Market Basics", 
                "2.2 Cryptocurrency Fundamentals & Wallets", 
                "2.3 Forex Market Structure & Currency Pairs", 
                "2.4 Commodities, Indices, and Futures"
            ],
            "Session 3: Brokers & Platforms": [
                "3.1 Choosing the Right Brokerage Account", 
                "3.2 Understanding Trading Fees and Commissions", 
                "3.3 Leverage, Margin, and Liquidation Risks", 
                "3.4 Navigating Trading Terminals and Chart Software"
            ],
            "Session 4: Market Participants": [
                "4.1 Retail Traders vs. Institutional Players", 
                "4.2 Central Banks and Macro Economic Drivers", 
                "4.3 Algorithmic and High-Frequency Trading (HFT)", 
                "4.4 Tracking Smart Money Movement"
            ],
            "Session 5: Day 1 Review & Practical Quiz": [
                "5.1 Order Execution Simulation Walkthrough", 
                "5.2 Interpreting Exchange Depth Charts", 
                "5.3 Avoiding Common Beginner Traps", 
                "5.4 Day 1 Knowledge Verification Checkpoint"
            ]
        },
        "Day 2: Price Action & Chart Reading": {
            "Session 1: Introduction to Price Action": [
                "1.1 What is Pure Price Action Analysis?", 
                "1.2 Stripping Away Indicator Clutter", 
                "1.3 Timeframes and Multi-Timeframe Analysis", 
                "1.4 The Concept of Market Memory"
            ],
            "Session 2: Support & Resistance": [
                "2.1 Identifying Key Horizontal Levels", 
                "2.2 Dynamic Support and Resistance Zones", 
                "2.3 How Round Numbers Act as Psychological Barriers", 
                "2.4 False Breakouts and Liquidity Sweeps"
            ],
            "Session 3: Trend Identification": [
                "3.1 Defining Bullish Market Structure (HH/HL)", 
                "3.2 Defining Bearish Market Structure (LH/LL)", 
                "3.3 Recognizing Consolidation and Ranging Markets", 
                "3.4 Trend Continuation vs. Reversal Signals"
            ],
            "Session 4: Chart Patterns Basics": [
                "4.1 Double Tops and Double Bottoms", 
                "4.2 Head and Shoulders Reversal Formations", 
                "4.3 Ascending, Descending, and Symmetrical Triangles", 
                "4.4 Bull and Bear Flags/Pennants"
            ],
            "Session 5: Day 2 Review & Chart Mapping": [
                "5.1 Mapping Key Levels on Real Assets", 
                "5.2 Spotting Structural Shifts in Real-Time", 
                "5.3 Handling Choppy and Sideways Markets", 
                "5.4 Day 2 Knowledge Verification Checkpoint"
            ]
        },
        "Day 3: Candlestick Mastery": {
            "Session 1: Candlestick Anatomy": [
                "1.1 Open, High, Low, Close (OHLC) Explained", 
                "1.2 Body Size vs. Wick Length Significations", 
                "1.3 Bullish vs. Bearish Momentum Bars", 
                "1.4 Understanding Volume Within Candles"
            ],
            "Session 2: Single Candle Reversals": [
                "2.1 Hammers and Hanging Mans", 
                "2.2 Shooting Stars and Inverted Hammers", 
                "2.3 The Power of Doji Indecision Candles", 
                "2.4 Marubozu Strong Momentum Candles"
            ],
            "Session 3: Multi-Candle Patterns": [
                "3.1 Bullish and Bearish Engulfing Patterns", 
                "3.2 Morning Star and Evening Star Formations", 
                "3.3 Harami Patterns and Inside Bars", 
                "3.4 Turch and Piercing Line Reversals"
            ],
            "Session 4: Contextual Candle Reading": [
                "4.1 Candlestick Placement at Key Support/Resistance", 
                "4.2 Rejecting Higher Prices: Long Upper Wicks", 
                "4.3 Accumulation Wicks at Bottoms", 
                "4.4 Reading Chain Reactions Across Multiple Candles"
            ],
            "Session 5: Day 3 Review & Pattern Recognition": [
                "5.1 Scanning Dashboards for High-Probability Candles", 
                "5.2 Avoiding Trap Patterns in Low-Volume Zones", 
                "5.3 Combining Candles with Structure", 
                "5.4 Day 3 Knowledge Verification Checkpoint"
            ]
        },
        "Day 4: Technical Indicators & Tools": {
            "Session 1: Moving Averages": [
                "1.1 Simple Moving Averages (SMA) Mechanics", 
                "1.2 Exponential Moving Averages (EMA) Weighting", 
                "1.3 Golden Cross and Death Cross Signifiers", 
                "1.4 Using MAs as Dynamic Support/Resistance"
            ],
            "Session 2: Momentum Oscillators": [
                "2.1 Relative Strength Index (RSI) Overbought/Oversold", 
                "2.2 Moving Average Convergence Divergence (MACD)", 
                "2.3 Stochastic Oscillator Deep Dive", 
                "2.4 Identifying Bullish and Bearish Divergences"
            ],
            "Session 3: Volume & Volatility Tools": [
                "3.1 Volume Profile and On-Balance Volume (OBV)", 
                "3.2 Bollinger Bands and Volatility Squeezes", 
                "3.3 Average True Range (ATR) for Volatility Tracking", 
                "3.4 Spotting Volume Spikes on Breakouts"
            ],
            "Session 4: Advanced Retracements": [
                "4.1 Fibonacci Retracement Levels (38.2%, 50%, 61.8%)", 
                "4.2 Pivot Point Calculations (Standard, Woodie, Camarilla)", 
                "4.3 Combining Indicators for Confluence", 
                "4.4 Avoiding Indicator Overload and Paralysis"
            ],
            "Session 5: Day 4 Review & Setup Building": [
                "5.1 Building a Multi-Indicator Dashboard Setup", 
                "5.2 Filtering False Signals with Volume", 
                "5.3 Backtesting Indicator Strategies Manually", 
                "5.4 Day 4 Knowledge Verification Checkpoint"
            ]
        },
        "Day 5: Risk Management & Capital Preservation": {
            "Session 1: The Golden Rule of Survival": [
                "1.1 Why 90% of Traders Lose Capital", 
                "1.2 Capital Preservation as Priority One", 
                "1.3 Calculating Risk Tolerance and Appetite", 
                "1.4 The Math of Drawdown Recovery"
            ],
            "Session 2: Position Sizing & Stop Losses": [
                "2.1 Defining the Hard Stop Loss", 
                "2.2 Risking 1% to 2% Per Trade Rule", 
                "2.3 Dynamic Position Sizing Formulas", 
                "2.4 Avoiding Emotional Stop Adjustments"
            ],
            "Session 3: Risk-to-Reward Ratios": [
                "3.1 Understanding 1:2 and 1:3 RR Targets", 
                "3.2 Win Rate vs. Risk-to-Reward Matrix", 
                "3.3 Scaling Out and Taking Partial Profits", 
                "3.4 Moving Stops to Break-Even Safely"
            ],
            "Session 4: Portfolio Allocation": [
                "4.1 Diversification Across Asset Classes", 
                "4.2 Handling Correlated Assets", 
                "4.3 Emergency Cash Reserves Management", 
                "4.4 Evaluating Overall Portfolio Exposure"
            ],
            "Session 5: Day 5 Review & Risk Calculation": [
                "5.1 Practical Position Sizing Exercises", 
                "5.2 Setting Up Automated Stop Protections", 
                "5.3 Stress Testing a Trading Portfolio", 
                "5.4 Day 5 Knowledge Verification Checkpoint"
            ]
        },
        "Day 6: Trading Psychology & Discipline": {
            "Session 1: Emotional Traps in Trading": [
                "1.1 Recognizing FOMO (Fear Of Missing Out)", 
                "1.2 Overcoming Greed and Unrealistic Expectations", 
                "1.3 Handling Panic and Fear of Execution", 
                "1.4 Understanding Hope as a Destructive Emotion"
            ],
            "Session 2: Revenge Trading & Tilt": [
                "1.2 What is Psychological 'Tilt'?", 
                "2.2 The Danger of Revenge Trading After Losses", 
                "2.3 Knowing When to Step Away from Screens", 
                "2.4 Resetting Mental Clarity Post-Drawdown"
            ],
            "Session 3: Discipline & Routine": [
                "3.1 Establishing a Pre-Market Routine", 
                "3.2 Sticking Strictly to the Trading Plan", 
                "3.3 Dealing with Winning and Losing Streaks", 
                "3.4 Cultivating Patience for High-Quality Setups"
            ],
            "Session 4: The Trading Journal": [
                "4.1 Why Every Professional Keeps a Journal", 
                "4.2 Tracking Metrics: Win Rate, RR, and Expectancy", 
                "4.3 Reviewing Mistakes and Psychological Triggers", 
                "4.4 Refining Strategy via Data Analytics"
            ],
            "Session 5: Day 6 Review & Mindset Check": [
                "5.1 Psychological Self-Assessment Framework", 
                "5.2 Crafting a Personal Discipline Code", 
                "5.3 Mindfulness and Focus Techniques for Traders", 
                "5.4 Day 6 Knowledge Verification Checkpoint"
            ]
        },
        "Day 7: Building Your Master Trading Plan": {
            "Session 1: Strategy Synthesis": [
                "1.1 Combining Technicals, Risk, and Psychology", 
                "1.2 Defining Your Personal Trading Style (Day vs. Swing)", 
                "1.3 Selecting Core Trading Instruments", 
                "1.4 Defining Clear Entry Triggers"
            ],
            "Session 2: Exit Strategies": [
                "2.1 Defining Profit Targets Before Entering", 
                "2.2 Trailing Stop Methodologies", 
                "2.3 Handling Sudden Market News Events", 
                "2.4 End-of-Day Position Management Rules"
            ],
            "Session 3: Backtesting & Forward Testing": [
                "3.1 Manual Backtesting Methodologies", 
                "3.2 Forward Testing via Paper Trading Simulators", 
                "3.3 Validating Strategy Edge Over 100 Trades", 
                "3.4 Tweaking Parameters Without Curve Fitting"
            ],
            "Session 4: Live Execution Framework": [
                "4.1 Step-by-Step Pre-Trade Checklist", 
                "4.2 Live Trade Execution Protocol", 
                "4.3 Post-Trade Debriefing Routine", 
                "4.4 Scaling Up Capital Gradually"
            ],
            "Session 5: Day 7 Review & Graduation": [
                "5.1 Final Masterclass Comprehensive Review", 
                "5.2 Finalizing Your Personal 3-Step Checklist", 
                "5.3 Transitioning from Paper Trading to Live Markets", 
                "5.4 Official TradeX Academy Graduation Checkpoint"
            ]
        }
    }

    # Displaying the Curriculum via Interactive Selectors and Expanders
    selected_day = st.selectbox("Select Day of the Masterclass", list(curriculum.keys()))
    
    st.markdown(f"---### 📌 {selected_day}")
    
    day_sessions = curriculum[selected_day]
    for session_name, lessons in day_sessions.items():
        with st.expander(f"📖 {session_name} (4 Lessons)"):
            for lesson in lessons:
                st.markdown(f"""
                <div class="lesson-item">
                    <span style="color: #2962ff; font-weight: bold;">Lesson Module</span>
                    <h4 style="color: #ffffff; margin: 5px 0;">{lesson}</h4>
                    <p style="color: #848e9c; font-size: 0.9rem; margin: 0;">Click 'Start Lesson' in your live interface or use your terminal workbook to study this module.</p>
                </div>
                """, unsafe_allow_html=True)

elif page == "Markets":
    st.title("Markets")
    st.info("The live markets database view is currently syncing.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.info("The paper trading execution engine is currently under development.")
    
