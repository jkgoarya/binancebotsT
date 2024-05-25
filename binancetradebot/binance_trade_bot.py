import logging
import time
from binancetradebot.starlight_strategy import StarlightStrategy

class BinanceTradeBot:
    def __init__(self, config):
        self.strategy = StarlightStrategy(config)
        self.fetch_interval_seconds = int(config.get('trading', 'fetch_interval_seconds', fallback=1))

    def run(self):
        symbols = self.strategy.config.get('trading', 'symbols').split(',')
        while True:
            self.strategy.scout(symbols)
            time.sleep(self.fetch_interval_seconds)
