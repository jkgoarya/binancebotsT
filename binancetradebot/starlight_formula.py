# starlight_formula.py
import pandas as pd
from binancetradebot.fetch_data import fetch_futures_data  # Ensure this import points to the correct module and function

class StarlightCalculator:
    def __init__(self, client, symbols):
        self.client = client
        self.symbols = symbols

    def calculate_starlight(self, P, K, I, c=1):
        """Calculate a composite score from momentum, trend, and innovation factors."""
        return (P + K) * I * (c ** 2)

    def calculate_indicators(self, df):
        """Calculate momentum, trend-following, and innovation indicators on the data frame."""
        df['P'] = df['close'].rolling(window=14).mean()
        df['K'] = df['close'].ewm(span=26, adjust=False).mean()
        df['I'] = df['close'].pct_change()
        return df

    def fetch_and_calculate(self):
        """Fetch data for each symbol and calculate the Starlight score."""
        results = {}
        for symbol in self.symbols:
            df = fetch_futures_data(self.client, symbol)
            if df.empty:
                print(f"No data fetched for {symbol}. Continuing to next symbol.")
                continue
            df = self.calculate_indicators(df)
            df['starlight_score'] = self.calculate_starlight(df['P'], df['K'], df['I'])
            results[symbol] = df
        return results
