import pandas as pd
from binance.client import Client
import logging

def fetch_data(symbol, interval, lookback, api_key, api_secret, retry_count=3):
    client = Client(api_key, api_secret)
    attempt = 0
    while attempt < retry_count:
        try:
            logging.info(f"Attempting to fetch data for {symbol} at {interval}, attempt {attempt + 1}")
            klines = client.get_historical_klines(symbol, interval, lookback)
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
            
            if df.empty:
                logging.warning(f"No data returned for {symbol}. Retrying...")
                attempt += 1
                continue

            logging.info(f"Data fetched successfully for {symbol}")
            return df
        except Exception as e:
            logging.error(f"Error fetching data for {symbol}: {e}")
            attempt += 1
            if attempt >= retry_count:
                logging.error(f"Failed to fetch data after {retry_count} attempts")
                break
            logging.info("Retrying after error...")
    return pd.DataFrame()  # Return an empty DataFrame if all attempts fail
