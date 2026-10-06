from typing import Any

products: list[Any] = []

def normalize_code(code) -> int:
    for product in products:
        if code == product["code"]:
            raise ValueError("The code is already registered.")
    if code.isdigit():
        raise ValueError("The code contains letters.")
    if code not in range(0,100):
        raise ValueError("The code is out of range.")
    return code

def valid_stock(stock) -> int:
    if not isinstance(stock, int):
        raise ValueError("Stock is not a number.")
    if stock < 0:
        raise ValueError("The stock cannot be less than 0")
    return stock

def valid_name(name) -> str:
    if not isinstance(name, str):
        raise ValueError("The name is not a word.")
    if not name.strip():
        raise ValueError("The name cannot be empty.")
    if len(name) < 3:
        raise ValueError("The name cannot be shorter than 3 letters.")
    return name

def build_product( name: str, code: int, stock: int) -> dict[str, Any] | None:
    try:
        code = normalize_code(code)
        name = valid_name(name)
        stock = valid_stock(stock)
        product = {
            "code" : code,
            "name" : name,
            "stock" : stock
        }
        return product
    except ValueError as error:
        print(error)

build_product(
    name = "Laptop",
    code = 12,
    stock = 25
)

print(products)