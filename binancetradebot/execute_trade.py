# execute_trade.py
def place_futures_order(client, symbol, quantity, side):
    """Place a futures market order."""
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        return order
    except Exception as e:
        print(f"Failed to place order: {e}")
        return None
