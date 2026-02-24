def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(qty):
    qty = float(qty)
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    return qty

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("LIMIT order requires price")
        return float(price)
    return None