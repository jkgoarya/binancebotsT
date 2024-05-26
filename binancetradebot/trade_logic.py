# trade_logic.py
from utils import get_current_price
from config import threshold_price

def should_buy(current_price):
    return current_price < threshold_price

def calculate_btc_purchase(investment, price):
    return investment / price
