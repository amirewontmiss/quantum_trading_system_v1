
import time
from trading_modules.data_fetching import fetch_crypto_data
from trading_modules.trade_execution import execute_crypto_trade
from trading_modules.models import model, agent, scaler

def live_trading(symbol="BTCUSDT", trading_hours=1):
    start_time = time.time()
    while time.time() - start_time < trading_hours * 3600:
        state = fetch_crypto_data(symbol)
        state_normalized = scaler.transform([state])
        signal = model.predict(state_normalized)[0]
        state_with_position = state + [0, 10000]  # Placeholder for position and balance
        action, _ = agent.predict(state_with_position)
        execute_crypto_trade(action, symbol=symbol, quantity=0.001)
        time.sleep(60)

if __name__ == "__main__":
    live_trading()
