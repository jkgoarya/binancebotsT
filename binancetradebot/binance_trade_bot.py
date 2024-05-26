import logging
import time
from binancetradebot.starlight_strategy import StarlightStrategy

class BinanceTradeBot:
    def __init__(self, config):
        self.strategy = StarlightStrategy(config)
        self.fetch_interval_seconds = int(config.get('trading', 'fetch_interval_seconds', fallback=60))

    def run(self):
        symbols = self.strategy.calculator.symbols
        while True:
            self.strategy.scout(symbols)
            time.sleep(self.fetch_interval_seconds)
