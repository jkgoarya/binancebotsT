import logging
from datetime import datetime

class PerformanceTracker:
    def __init__(self):
        self.trades = []

    def record_trade(self, symbol, side, price, quantity):
        trade = {
            'symbol': symbol,
            'side': side,
            'price': price,
            'quantity': quantity,
            'timestamp': datetime.now()
        }
        self.trades.append(trade)
        logging.info(f"Trade recorded: {trade}")

    def get_performance(self):
        profit_loss = 0
        for trade in self.trades:
            if trade['side'] == 'BUY':
                profit_loss -= trade['price'] * trade['quantity']
            elif trade['side'] == 'SELL':
                profit_loss += trade['price'] * trade['quantity']
        logging.info(f"Current profit/loss: {profit_loss}")
        return profit_loss

    def get_summary_stats(self):
        total_profit = sum(trade['price'] * trade['quantity'] if trade['side'] == 'SELL' else -trade['price'] * trade['quantity'] for trade in self.trades)
        number_of_trades = len(self.trades)
        average_profit_per_trade = total_profit / number_of_trades if number_of_trades > 0 else 0
        return {
            "total_profit": total_profit,
            "number_of_trades": number_of_trades,
            "average_profit_per_trade": average_profit_per_trade
        }

# Example of setting up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
