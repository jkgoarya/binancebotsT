import logging
from binance.client import Client

def place_trade(api_key, api_secret, symbol, side, quantity):
    client = Client(api_key, api_secret)
    try:
        # Assume MARKET order for simplicity
        order = client.order_market(symbol=symbol, side=side, quantity=quantity)
        logging.info(f"Order placed successfully: {order}")
        return order
    except Exception as e:
        logging.error(f"Failed to place order for {symbol}: {e}")
        return None

def cancel_order(api_key, api_secret, symbol, order_id):
    client = Client(api_key, api_secret)
    try:
        result = client.cancel_order(symbol=symbol, orderId=order_id)
        logging.info(f"Order {order_id} canceled successfully: {result}")
        return True
    except Exception as e:
        logging.error(f"Failed to cancel order {order_id} for {symbol}: {e}")
        return False
