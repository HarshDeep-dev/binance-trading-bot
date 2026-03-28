import typer
import logging
from bot.client import BinanceClient
from bot.logging_config import setup_logging

app = typer.Typer()
setup_logging()

API_KEY = "PASTE_YOUR_TESTNET_KEY_HERE"
API_SECRET = "PASTE_YOUR_TESTNET_SECRET_HERE"

@app.command()
def trade(
    symbol: str = typer.Option(..., help="Symbol like BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Amount to trade"),
    price: float = typer.Option(None, help="Price (only for LIMIT)")
):
    client = BinanceClient(API_KEY, API_SECRET)
    
    try:
        logging.info(f"Attempting {side} {order_type} for {quantity} {symbol}")
        response = client.place_order(symbol, side, order_type, quantity, price)
        
        
        typer.secho(f"✅ Success! Order ID: {response.get('orderId')}", fg=typer.colors.GREEN)
        typer.echo(f"Status: {response.get('status')}")
        typer.echo(f"Price: {response.get('avgPrice', price)}")
        
    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        typer.secho(f"❌ Failed: {str(e)}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()