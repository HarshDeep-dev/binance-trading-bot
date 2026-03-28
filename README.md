
# Binance Futures Trading Bot (Testnet)

A Python-based CLI tool to place Market and Limit orders on the Binance Futures Testnet.

## Security Note
**Important:** API Keys have been removed for security. To test this bot, you must add your own Binance Testnet API credentials to the `API_KEY` and `API_SECRET` variables in `cli.py`.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

Usage Examples
Use the following commands in your terminal to place orders:

Market Order:
python3 cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.002

Limit Order:
python3 cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.002 --price 75000

Key Features & Error Handling
This is where you show off your work. Mention the specific things you solved.

Project Highlights
Modular Structure: Separated the API logic (client.py) from the user interface (cli.py) for better reusability.

Automated Logging: All requests, successful responses, and errors are saved in bot.log.

Robust Error Handling: The bot handles real-world API restrictions like:

Notional Value: Prevents orders below the $100 minimum.

Price Filters: Ensures Limit prices are valid based on current market data.

Assumptions ~
The user has a Binance Futures Testnet account with a USDT balance.

The python-binance library is used for stable API communication.
