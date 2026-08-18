import time
import random
import json
import os

# ==========================================
# GIPSY-AI TRADING SIMULATOR & CLI DASHBOARD
# Designed for Pydroid 3 & GitHub Actions / Streamlit
# ==========================================

LOG_FILE = "trades.json"

def initialize_journal():
    """Ensure the trade journal log file exists."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

def load_trades():
    """Load saved trades from local storage."""
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_trade(trade_data):
    """Append a new trade to the JSON log file."""
    trades = load_trades()
    trades.append(trade_data)
    with open(LOG_FILE, "w") as f:
        json.dump(trades, f, indent=4)

def calculate_sma(prices, period):
    """Calculate Simple Moving Average using built-in math."""
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

def run_simulation_step(current_prices, resistance):
    """Simulate a single price tick and check for breakout conditions."""
    latest_price = round(random.uniform(95.0, 115.0), 2)
    current_prices.append(latest_price)
    
    # Keep only the last 20 periods for memory efficiency
    if len(current_prices) > 20:
        current_prices.pop(0)
        
    sma_3 = calculate_sma(current_prices, 3)
    
    print(f"\n[Tick] Price: {latest_price} | SMA(3): {sma_3}")
    
    # Breakout & Crossover Logic
    if sma_3 and latest_price > resistance:
        print(f"🚨 BREAKOUT SIGNAL DETECTED at {latest_price} (Resistance: {resistance})")
        trade = {
            "timestamp": time.time(),
            "entry_price": latest_price,
            "status": "BUY_SIGNAL"
        }
        save_trade(trade)
        return True
    return False

def main():
    print("==========================================")
    print("  GIPSY-AI: MOBILE TRADING BOT SIMULATOR  ")
    print("==========================================")
    
    initialize_journal()
    price_history = [100.0, 101.5, 102.0]
    resistance_level = 108.0
    
    print(f"Monitoring asset against resistance: {resistance_level}")
    print("Running 5 simulation cycles...\n")
    
    for step in range(1, 6):
        print(f"--- Cycle {step} of 5 ---")
        run_simulation_step(price_history, resistance_level)
        time.sleep(1) # Simulate real-time delay
        
    print("\nSimulation complete. Logged trades summary:")
    saved_trades = load_trades()
    print(json.dumps(saved_trades, indent=4))

if __name__ == "__main__":
    main()
  
