from binance import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        # Setting testnet=True is critical for the assignment
        self.client = Client(api_key, api_secret, testnet=True)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }
        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC" # Good Till Cancelled
        
        return self.client.futures_create_order(**params)