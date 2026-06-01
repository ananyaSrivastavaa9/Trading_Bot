# Binance Futures Testnet Trading Bot

## What this project does
A small Python CLI app that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- BUY and SELL support
- MARKET and LIMIT orders
- CLI input validation
- Request/response logging
- Error handling

## Setup
1. Create a Binance Futures Testnet account.
2. Add API key and secret in `.env`.
3. Create virtual env:
   python -m venv .venv
4. Activate it.
5. Install dependencies:
   pip install -r requirements.txt

## Run
Market order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000

## Assumptions
- Using Binance Futures Testnet.
- LIMIT orders require price.
- Orders are placed on USDT-M futures testnet.

## Logs
Logs are saved in:
logs/bot.log