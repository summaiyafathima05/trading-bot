from typing import Optional

from client import BinanceClient, BinanceClientError
from logging_config import setup_logger
from validators import (
   ValidationError,
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

logger = setup_logger("orders")
 

def place_order(
    client: BinanceClient,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float] = None,
) -> None:
    """Validate inputs, place the order, and print a clear summary."""

    # --- Validate ---
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)
    except ValidationError as exc:
        logger.error("Validation failed: %s", exc)
        print(f"\n❌  Validation Error: {exc}\n")
        return

    # --- Summary before placing ---
    print("\n" + "─" * 50)
    print("  ORDER REQUEST SUMMARY")
    print("─" * 50)
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Type       : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price is not None:
        print(f"  Price      : {price}")
    print("─" * 50)

    # --- Place order ---
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )
    except BinanceClientError as exc:
        logger.error("Order failed: %s", exc)
        print(f"\n❌  Order Failed: {exc}\n")
        return

    # --- Print response ---
    order_id = response.get("orderId", "N/A")
    status = response.get("status", "N/A")
    executed_qty = response.get("executedQty", "N/A")
    avg_price = response.get("avgPrice", None)

    print("\n  ORDER RESPONSE")
    print("─" * 50)
    print(f"  Order ID     : {order_id}")
    print(f"  Status       : {status}")
    print(f"  Executed Qty : {executed_qty}")
    if avg_price is not None:
        print(f"  Avg Price    : {avg_price}")
    print("─" * 50)
    print("  ✅  Order placed successfully!\n")

    logger.info(
        "Order placed successfully | orderId=%s status=%s executedQty=%s avgPrice=%s",
        order_id,
        status,
        executed_qty,
        avg_price,
    )
