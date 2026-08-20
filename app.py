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
    .lesson-card {
        background-color: #1e222d;
        border: 1px solid #2a2e39;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .lesson-card:hover {
        border-color: #2962ff;
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

# Sidebar Navigation matching the TradeX layout
st.sidebar.markdown("## TRADE<span style='color: #2962ff;'>X</span>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Trading Academy (Learn)", "Markets", "Paper Trading"])

if page == "Dashboard":
    # Header Section
    st.markdown("<p style='color: #848e9c; margin-bottom: 0;'>WELCOME BACK</p>", unsafe_allow_html=True)
    st.title("Trading Dashboard")
    
    # Top Metric Cards
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

    st.write("") # Spacer

    # Main Content Layout: Chart & Watchlist
    chart_col, watch_col = st.columns([3, 1])
    
    with chart_col:
        st.markdown("### BTC / USD")
        st.markdown("## $68,420.50")
        
        # Timeframe selector simulation
        cols = st.columns([1, 1, 1, 1, 6])
        with cols[0]: st.button("1H")
        with cols[1]: st.button("1D", type="primary")
        with cols[2]: st.button("1W")
        with cols[3]: st.button("1M")
        
        # Clean line chart generation without any backend debug text leaks
        chart_data = pd.DataFrame(
            np.random.randn(50, 1).cumsum() + 68420,
            columns=["Price"]
        )
        st.line_chart(chart_data, color="#2962ff", height=350)
        
    with watch_col:
        st.markdown("### Watchlist")
        watchlist_items = {
            "BTC": "$68,420",
            "ETH": "$3,420",
            "AAPL": "$227.10",
            "TSLA": "$341.20"
        }
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
    st.write("Master the markets day-by-day with our structured curriculum.")
    
    lessons = [
        ("Day 1", "Introduction to Financial Markets", "Learn how markets work, explore asset classes like Stocks and Crypto, and understand the core mechanics of buyers, sellers, and order types."),
        ("Day 2", "Reading the Tape & Price Action", "Understand how price moves naturally over time by mastering support, resistance levels, and interpreting momentum without complex indicators."),
        ("Day 3", "Mastering Candlestick Charts", "Break down the anatomy of a single candlestick (OHLC), wicks versus bodies, and spot powerful reversal patterns like hammers and dojis."),
        ("Day 4", "Trend Analysis & Market Structure", "Identify market direction to trade with the momentum. Learn to spot bull markets, bear markets, and sideways consolidation ranges."),
        ("Day 5", "Risk Management & Capital Preservation", "The golden rule of trading: survive to trade another day. Learn risk-to-reward ratios, position sizing, and how to protect your portfolio."),
        ("Day 6", "Psychology of a Trader", "Master your emotions. Learn how to conquer FOMO, greed, and panic, avoid revenge trading, and maintain absolute discipline."),
        ("Day 7", "Building Your First Trading Plan", "Combine technical analysis, execution rules, and risk management into a concrete personal checklist you can rely on every single day.")
    ]
    
    for day, title, desc in lessons:
        st.markdown(f"""
        <div class="lesson-card">
            <span style="background: rgba(41, 98, 255, 0.15); color: #2962ff; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; font-weight: bold;">{day}</span>
            <h3 style="margin-top: 10px; color: #ffffff; margin-bottom: 8px;">{title}</h3>
            <p style="color: #848e9c; margin-bottom: 0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Markets":
    st.title("Markets")
    st.info("The live markets database view is currently syncing.")

elif page == "Paper Trading":
    st.title("Paper Trading Simulator")
    st.info("The paper trading execution engine is currently under development.")
            
