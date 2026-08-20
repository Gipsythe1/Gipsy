import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="TradeX",
    page_icon="📈",
    layout="wide"
)

# Custom Styling to Match TradeX Dark Theme
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
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("# **TRADE<span style='color: #2962ff;'>X</span>**", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Learn (7-Day Curriculum)", "Markets", "Paper Trading"])

if page == "Dashboard":
    # Header Section
    st.markdown("### WELCOME BACK")
    st.title("Trading Dashboard")
    
    # Top Metric Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px;">Portfolio Value</p>
            <h2 style="margin: 0; color: #ffffff;">$10,000.00</h2>
            <span style="color: #089981; font-weight: bold;">+2.45%</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px;">Today's Profit</p>
            <h2 style="margin: 0; color: #ffffff;">$245.60</h2>
            <span style="color: #089981; font-weight: bold;">+2.45%</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #848e9c; margin-bottom: 5px;">Available Cash</p>
            <h2 style="margin: 0; color: #ffffff;">$8,750.00</h2>
            <span style="color: #848e9c;">Ready to trade</span>
        </div>
        """, unsafe_allow_html=True)

    st.write("") # Spacer

    # Main Content Layout: Chart & Watchlist
    chart_col, watch_col = st.columns([3, 1])
    
    with chart_col:
        st.markdown("### BTC / USD")
        st.markdown("## $68,420.50")
        
        # Generate dummy price data for chart
        chart_data = pd.DataFrame(
            np.random.randn(50, 1).cumsum() + 68420,
            columns=["Price"]
        )
        st.line_chart(chart_data, color="#2962ff")
        
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
            <div style="background: #1e222d; padding: 10px 15px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between;">
                <b>{asset}</b>
                <span style="color: #848e9c;">{price}</span>
            </div>
            """, unsafe_allow_html=True)

elif page == "Learn (7-Day Curriculum)":
    st.markdown("### TRADING ACADEMY")
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
            <h3 style="margin-top: 10px; color: #ffffff;">{title}</h3>
            <p style="color: #848e9c;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page in ["Markets", "Paper Trading"]:
    st.title(f"{page}")
    st.info(f"The {page.lower()} module is currently under development.")
        
