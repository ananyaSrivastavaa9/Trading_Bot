import argparse

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.orders import place_order


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol like BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Required for LIMIT order")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None
        if order_type == "LIMIT":
            price = validate_price(args.price)

        print("\nOrder Request Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price is not None:
            print(f"Price: {price}")

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\nOrder Response Details")
        print(f"orderId: {response.get('orderId')}")
        print(f"status: {response.get('status')}")
        print(f"executedQty: {response.get('executedQty')}")
        print(f"avgPrice: {response.get('avgPrice', 'N/A')}")
        print("\nSuccess: Order placed successfully")

    except Exception as e:
        print(f"\nFailure: {str(e)}")


if __name__ == "__main__":
    main()