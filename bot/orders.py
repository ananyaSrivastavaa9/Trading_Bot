from bot.client import BinanceClient

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):
    response = client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )
    return response