import logging
from binancetradebot.config import load_config
from binancetradebot.binance_trade_bot import BinanceTradeBot

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    config = load_config('config.ini', 'secret.cfg')
    bot = BinanceTradeBot(config)
    bot.run()
