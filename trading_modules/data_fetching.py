
from binance.client import Client

api_key = "YOUR_BINANCE_API_KEY"
api_secret = "YOUR_BINANCE_API_SECRET"
client = Client(api_key, api_secret)

def fetch_crypto_data(symbol="BTCUSDT"):
    klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=1)
    latest_kline = klines[-1]
    open_price, high_price, low_price, close_price, volume = map(float, latest_kline[1:6])
    return [open_price, high_price, low_price, close_price, volume]
