# Binance Futures Testnet Trading Bot

## Setup
1. Create Binance Futures Testnet account
2. Add API keys in .env
3. pip install -r requirements.txt

## Run
Market:
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit:
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000

## Assumptions
Testnet only.