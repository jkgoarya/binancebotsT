import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from binancetradebot.fetch_data import fetch_data

class StarlightCalculator:
    def __init__(self, symbols):
        self.symbols = symbols

    def calculate_starlight(self, P, K, I, c=1):
        """ Calculate a composite score from momentum, trend, and innovation factors. """
        return (P + K) * I * (c ** 2)

    def calculate_indicators(self, df):
        """ Calculate momentum, trend-following, and innovation indicators. """
        df['P'] = df['close'].rolling(window=14).mean()
        df['K'] = df['close'].ewm(span=26, adjust=False).mean()
        df['I'] = df['close'].pct_change()
        return df

    def fetch_and_calculate(self):
        results = {}
        for symbol in self.symbols:
            df = fetch_data(symbol=symbol)
            if df.empty:
                print(f"No data fetched for {symbol}.")
                continue
            df = self.calculate_indicators(df)
            df['starlight_score'] = self.calculate_starlight(df['P'], df['K'], df['I'])
            results[symbol] = df
        return results

    def plot_scores(self, results):
        for symbol, df in results.items():
            plt.figure(figsize=(10, 6))
            plt.plot(df['starlight_score'], label='Starlight Score')
            plt.axhline(y=70, color='r', linestyle='--', label='Sell Threshold')
            plt.axhline(y=30, color='g', linestyle='--', label='Buy Threshold')
            plt.title(f'Starlight Scores for {symbol}')
            plt.legend()
            plt.savefig(f'plots/starlight_scores_{symbol}.png')
            plt.show()

# Usage
if __name__ == "__main__":
    symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "AVAXUSDT"]
    calc = StarlightCalculator(symbols)
    results = calc.fetch_and_calculate()
    calc.plot_scores(results)
