# curriculum.py

lessons_db = {
    "M1 W1 D1: Bid-Ask Spreads": {
        "concept": "Order books, market makers, and liquidity mechanics.",
        "questions": [
            {
                "question": "What is the primary role of a Market Maker?",
                "options": ["Crash price", "Provide liquidity", "Charge high taxes", "Print money"],
                "answer": "Provide liquidity"
            },
            {
                "question": "What is the 'Bid' price in an order book?",
                "options": ["The price sellers are asking for", "The highest price a buyer is willing to pay", "The historical average price", "The closing price of the day"],
                "answer": "The highest price a buyer is willing to pay"
            }
        ]
    },
    "M1 W1 D2: Market vs Limit Orders": {
        "concept": "Execution types, slippage, and order routing.",
        "questions": [
            {
                "question": "Which order type guarantees execution speed over price?",
                "options": ["Limit Order", "Stop Loss", "Market Order", "Trailing Stop"],
                "answer": "Market Order"
            },
            {
                "question": "What risk do you take when placing a Market Order in low-liquidity assets?",
                "options": ["Slippage", "Zero commission", "Exchange bankruptcy", "Dividend cuts"],
                "answer": "Slippage"
            }
        ]
    },
    "M1 W2 D1: Support & Resistance": {
        "concept": "Key price levels, psychological barriers, and liquidity pools.",
        "questions": [
            {
                "question": "What typically happens when a resistance level is decisively broken?",
                "options": ["It acts as a new support level", "Trading is suspended", "Volume drops to zero", "The asset becomes illegal"],
                "answer": "It acts as a new support level"
            }
        ]
    },
    "M2 W1 D1: Risk-to-Reward Ratio": {
        "concept": "Position sizing, expectancy, and managing downside exposure.",
        "questions": [
            {
                "question": "If you risk $100 to make $300, what is your Risk-to-Reward ratio?",
                "options": ["1:1", "1:2", "1:3", "3:1"],
                "answer": "1:3"
            }
        ]
    }
}
