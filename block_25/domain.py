def validate_product(name, stock, price):
    if len(name) < 3 or not name.strip():
        raise ValueError("ERROR: Name no valid.")

    if stock < 0:
        raise ValueError("ERROR: Stock invalid.")

    if price < 0:
        raise ValueError("ERROR: Price.") 

    return name, stock, price


def create_product(name, stock, price):
    name, stock, price = validate_product(name,stock, price)

    product = {
        "name" : name,
        "stock" : stock,
        "price" : price,
    }
    return product