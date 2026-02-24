from .client import get_client
from .logging_config import setup_logger

logger = setup_logger()
client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):

    try:
        logger.info(f"Request: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(str(e))
        raise