# binancetradebot/auto_trader.py

import logging
import pandas as pd
from binance.client import Client
from binancetradebot.config import load_config

# Setup logging at the module level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AutoTrader:
    def __init__(self, config):
        self.config = config
        self.api_key = config.get('BINANCE', 'API_KEY')
        self.api_secret = config.get('BINANCE', 'API_SECRET')
        self.client = Client(self.api_key, self.api_secret)

    def get_historical_data(self, symbol, interval=Client.KLINE_INTERVAL_1MINUTE, lookback='1 day ago UTC'):
        try:
            klines = self.client.get_historical_klines(symbol, interval, lookback)
            df = pd.DataFrame(klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_asset_volume', 'number_of_trades',
                'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
            ])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            numeric_cols = ['open', 'high', 'low', 'close', 'volume', 
                            'quote_asset_volume', 'taker_buy_base_asset_volume', 
                            'taker_buy_quote_asset_volume']
            df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
            logger.info(f"Historical data fetched successfully for {symbol}")
            return df
        except Exception as e:
            logger.error(f"Failed to fetch historical data for {symbol}: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
