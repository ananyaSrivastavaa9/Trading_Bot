def validate_symbol(symbol: str) -> str:
    if not symbol or not symbol.strip():
        raise ValueError("symbol is required")
    return symbol.strip().upper()

def validate_side(side: str) -> str:
    side = side.strip().upper()
    if side not in {"BUY", "SELL"}:
        raise ValueError("side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.strip().upper()
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(quantity) -> float:
    qty = float(quantity)
    if qty <= 0:
        raise ValueError("quantity must be greater than 0")
    return qty

def validate_price(price) -> float:
    if price is None or price == "":
        raise ValueError("price is required for LIMIT order")
    p = float(price)
    if p <= 0:
        raise ValueError("price must be greater than 0")
    return p