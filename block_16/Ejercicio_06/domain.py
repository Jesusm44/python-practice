from typing import Any
# With this function we validate the stock: no 1. we do a try/except to check that the code is a number.
#Then we make two conditions:
#1. Check that the code is in a range from 1 to 100
#2. That the code is not registered
def _validation_code(products, code) -> int:
    try:
        validate_code = int(code)
    except ValueError:
        raise ValueError("The code must be an integer.")

    if validate_code not in range(0,101):
        raise ValueError("The code cannot be less than 0.")

    result:list[Any] = list(filter(
        lambda product: product["code"] == validate_code, products
    ))

    if not result:
        raise ValueError("The code already exists.")

    return validate_code

# This function helps us validate the names. number:
# 1. we check that the type is correct
# 2. We check that the name is not empty
# 3. It must have a certain number of characters, otherwise it will not be valid
# 4. check that they are only letters
# 5. We return the name in capital letters
def _validation_name(name) -> str:
    if not isinstance(name, str):
        raise TypeError("The name must be a string")
    if not name.strip():
            raise ValueError("The name cannot be empty.")
    if len(name) < 3:
        raise ValueError("The name cannot be less than 3 characters long.")
    if  not name.isalpha():
        raise ValueError("The name cannot contain numbers.")
    
    return name.capitalize()

# With this function we validate the stock: no 1. we do a try/except to check that the price is a number, and we use a validation, so that the price is never less than 0
def _validation_price(price) -> float:
    try:
        validation_price = float(price)
    except ValueError:
        raise ValueError("The value must be an integer or a decimal number.")
    if validation_price < 0:
        raise ValueError("The price cannot be less than 0")
    return validation_price

# With this function we validate the stock: no 1. we do a try/except to check that the stock is a number, and we use a validation, so that the stock is never less than 0
def _validation_stock(stock) -> int:
    try:
        validation_stock = int(stock)
    except ValueError:
        raise ValueError("The value must be an integer.")
    if validation_stock < 0:
        raise ValueError("The stock cannot be less than 0")
    return validation_stock