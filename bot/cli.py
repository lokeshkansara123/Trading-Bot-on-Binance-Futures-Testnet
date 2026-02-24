import argparse
from .orders import place_order
from .validators import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side.upper())
        order_type = validate_order_type(args.type.upper())
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\nOrder Summary:")
        print(symbol, side, order_type, quantity, price)

        order = place_order(symbol, side, order_type, quantity, price)

        print("\nOrder Response:")
        print("OrderId:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("ExecutedQty:", order.get("executedQty"))
        print("AvgPrice:", order.get("avgPrice"))

        print("\n✅ SUCCESS")

    except Exception as e:
        print("\n❌ FAILED:", str(e))


if __name__ == "__main__":
    main()