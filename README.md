# Trading_Bot

A simple Python CLI trading bot for Binance Futures Testnet.

## Features
- MARKET and LIMIT orders
- BUY and SELL support
- CLI validation
- Logging and error handling

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   pip install -r requirements.txt
3. Add API credentials in `.env`.

## Run
Market:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000

## Logs
Logs are saved in `logs/bot.log`.