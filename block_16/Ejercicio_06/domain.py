from typing import Any

def validation_code(products, code) -> int:
    try:
        validate_code = int(code)
    except ValueError:
        raise ValueError("The code must be an integer.")

    if validate_code not in range(0,101):
        raise ValueError("The code cannot be less than 0.")

    result:filter[Any] = filter(
        lambda product: product["code"] == validate_code, products
    )

    if result:
        raise ValueError("The code already exists.")

    return validate_code

def validation_name(name) -> str:
    if not isinstance(name, str):
        raise TypeError("The name must be a string")
    if not name.strip():
            raise ValueError("The name cannot be empty.")
    if len(name) < 3:
        raise ValueError("The name cannot be less than 3 characters long.")
    if  not name.isalpha():
        raise ValueError("The name cannot contain numbers.")
    
    return name.capitalize()

def validation_price(price) -> float:
    try:
        validation_price = float(price)
    except ValueError:
        raise ValueError("The value must be an integer or a decimal number.")

    if validation_price < 0:
        raise ValueError("The price cannot be less than 0")

    return validation_price

def validation_stock(stock) -> int:
    