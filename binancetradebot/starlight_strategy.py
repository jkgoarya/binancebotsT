import logging
from datetime import datetime, timedelta
from binancetradebot.execute_trade import place_trade, cancel_order
from binancetradebot.starlight_formula import StarlightCalculator

class StarlightStrategy:
    def __init__(self, config):
        self.api_key = config.get('BINANCE', 'API_KEY')
        self.api_secret = config.get('BINANCE', 'API_SECRET')
        self.buy_timeout = int(config.get('trading', 'buy_timeout', fallback=60))
        self.sell_timeout = int(config.get('trading', 'sell_timeout', fallback=60))
        self.last_buy_time = datetime.now()  # Initialize last_buy_time
        self.last_sell_time = datetime.now()  # Initialize last_sell_time
        self.calculator = StarlightCalculator(config.get('trading', 'symbols').split(','))

    def scout(self, symbols):
        results = self.calculator.fetch_and_calculate()
        for symbol, df in results.items():
            latest_score = df['starlight_score'].iloc[-1]
            if latest_score > 50:
                self.execute_trade(symbol, 'BUY')
            elif latest_score < -50:
                self.execute_trade(symbol, 'SELL')

    def execute_trade(self, symbol, trade_type):
        now = datetime.now()
        last_trade_time = getattr(self, f'last_{trade_type.lower()}_time', now)
        timeout = getattr(self, f'{trade_type.lower()}_timeout')

        if (now - last_trade_time).total_seconds() > timeout:
            quantity = 0.01  # Ensure this is set appropriately.
            order_id = place_trade(self.api_key, self.api_secret, symbol, trade_type, quantity)
            if order_id:
                logging.info(f"{trade_type} order placed for {symbol} with ID {order_id}")
                setattr(self, f'last_{trade_type.lower()}_time', now)
        else:
            logging.info(f"{trade_type} action skipped due to timeout for {symbol}")

# Ensure that other parts of your code match this structure
