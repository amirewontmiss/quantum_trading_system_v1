
from binance.client import Client

api_key = "YOUR_BINANCE_API_KEY"
api_secret = "YOUR_BINANCE_API_SECRET"
client = Client(api_key, api_secret)

def execute_crypto_trade(action, symbol="BTCUSDT", quantity=0.001):
    if action == 1:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print(f"Executed Buy Order: {order}")
    elif action == 2:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print(f"Executed Sell Order: {order}")
