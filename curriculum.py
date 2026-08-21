# utils/curriculum.py

lessons_db = {
    "1. Introduction to Financial Markets": {
        "concept": "Understanding how markets work, asset classes (stocks, crypto, forex), and what drives price action (supply and demand).",
        "questions": [
            {
                "question": "What is the primary driver of asset price movement in a free market?",
                "options": [
                    "Government decree",
                    "Supply and Demand",
                    "The number of employees in a company",
                    "Brokerage fees"
                ],
                "answer": "Supply and Demand"
            },
            {
                "question": "Which of the following is considered a decentralized digital asset class?",
                "options": [
                    "U.S. Treasury Bonds",
                    "Cryptocurrency",
                    "Blue-chip Stocks",
                    "Forex Fiat Currencies"
                ],
                "answer": "Cryptocurrency"
            },
            {
                "question": "What does 'liquidity' mean in the context of trading markets?",
                "options": [
                    "How quickly and easily an asset can be bought or sold without drastically changing its price",
                    "The amount of cash a broker holds in reserve",
                    "The humidity level on the trading floor",
                    "The dividend payout frequency"
                ],
                "answer": "How quickly and easily an asset can be bought or sold without drastically changing its price"
            }
        ]
    },
    "2. Reading Price Action & Candlesticks": {
        "concept": "Decoding Japanese candlesticks, open/high/low/close (OHLC) data, and basic trend structures.",
        "questions": [
            {
                "question": "On a standard green (bullish) candlestick, what does the bottom of the body represent?",
                "options": [
                    "The Close",
                    "The Open",
                    "The High",
                    "The absolute low of the day"
                ],
                "answer": "The Open"
            },
            {
                "question": "What do long upper wicks (shadows) on a candlestick generally indicate?",
                "options": [
                    "Strong buying pressure pushing prices higher",
                    "Selling pressure rejecting higher prices",
                    "Market closure",
                    "Zero market volatility"
                ],
                "answer": "Selling pressure rejecting higher prices"
            },
            {
                "question": "What defines an uptrend in market structure?",
                "options": [
                    "Lower highs and lower lows",
                    "Higher highs and higher lows",
                    "Sideways movement with equal prices",
                    "Random price swings"
                ],
                "answer": "Higher highs and higher lows"
            }
        ]
    },
    "3. Support and Resistance": {
        "concept": "Identifying key psychological price levels where buying or selling pressure historically accumulates.",
        "questions": [
            {
                "question": "What is a 'Support' level?",
                "options": [
                    "A price ceiling where sellers usually take over",
                    "A price floor where buying interest tends to be strong enough to overcome selling pressure",
                    "The average price of an asset over 200 days",
                    "A government subsidy for traders"
                ],
                "answer": "A price floor where buying interest tends to be strong enough to overcome selling pressure"
            },
            {
                "question": "What typically happens when a resistance level is decisively broken with high volume?",
                "options": [
                    "The asset becomes worthless",
                    "It often flips and acts as a new support level",
                    "Trading is suspended indefinitely",
                    "Sellers completely disappear forever"
                ],
                "answer": "It often flips and acts as a new support level"
            },
            {
                "question": "Why are round numbers (like $50,000 for Bitcoin or $100 for a stock) often powerful support/resistance zones?",
                "options": [
                    "Because exchanges highlight them in red",
                    "Psychologically, humans naturally place orders and stop losses around clean whole numbers",
                    "Math laws require prices to bounce there",
                    "They have no real significance"
                ],
                "answer": "Psychologically, humans naturally place orders and stop losses around clean whole numbers"
            }
        ]
    },
    "4. Risk Management & Position Sizing": {
        "concept": "Protecting capital using stop losses, risk-to-reward ratios, and the 1% rule.",
        "questions": [
            {
                "question": "What is the primary purpose of setting a 'Stop Loss' order?",
                "options": [
                    "To guarantee maximum profits on every trade",
                    "To automatically limit potential losses if the market moves against your position",
                    "To pay lower commission fees to your broker",
                    "To hide your trade size from other market participants"
                ],
                "answer": "To automatically limit potential losses if the market moves against your position"
            },
            {
                "question": "What does a 1:3 Risk-to-Reward ratio mean?",
                "options": [
                    "You risk $3 to potentially make $1",
                    "You risk $1 to potentially make $3",
                    "You lose 3 trades for every 1 win",
                    "Your broker takes a 3% cut of profits"
                ],
                "answer": "You risk $1 to potentially make $3"
            },
            {
                "question": "What is the general golden rule for capital preservation per individual trade among professional risk managers?",
                "options": [
                    "Risking no more than 1% to 2% of total trading capital on a single trade",
                    "Investing 100% of your net worth into a single breakout stock",
                    "Never using stop losses",
                    "Trading only on weekends"
                ],
                "answer": "Risking no more than 1% to 2% of total trading capital on a single trade"
            }
        ]
    },
    "5. Introduction to Technical Indicators": {
        "concept": "Using Moving Averages, RSI, and MACD to filter noise and gauge momentum.",
        "questions": [
            {
                "question": "What does RSI (Relative Strength Index) measure?",
                "options": [
                    "The velocity and magnitude of directional price movements to identify overbought or oversold conditions",
                    "The exact amount of shares outstanding",
                    "The daily trading volume in dollars",
                    "The interest rate set by the Federal Reserve"
                ],
                "answer": "The velocity and magnitude of directional price movements to identify overbought or oversold conditions"
            },
            {
                "question": "An RSI reading above 70 typically suggests an asset is:",
                "options": [
                    "Oversold and due for a bounce",
                    "Overbought and potentially due for a pullback or consolidation",
                    "Trading exactly at fair value",
                    "Delisted from the exchange"
                ],
                "answer": "Overbought and potentially due for a pullback or consolidation"
            },
            {
                "question": "What is a Moving Average (MA) primarily used for?",
                "options": [
                    "Smoothing out price data to help identify the prevailing market trend direction",
                    "Predicting exact future stock prices down to the second",
                    "Calculating corporate earnings reports",
                    "Determining tax liabilities"
                ],
                "answer": "Smoothing out price data to help identify the prevailing market trend direction"
            }
        ]
    }
}
