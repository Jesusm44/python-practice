import pathlib
import json

from domain import (
    _validation_code,
    _validation_name,
    _validation_price,
    _validation_stock,
)


DIR = pathlib.Path(__file__).parent / "data"
DIR.mkdir(parents=True, exist_ok=True)

FILE = DIR / "products.json"


def save_products(products) -> None:
    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as archive:
        json.dump(products, archive, indent=4)


def save_product(products: list, code, name, price, stock) -> None:
    # Validate each product field before saving it.
    code = _validation_code(products, code)
    name = _validation_name(name)
    price = _validation_price(price)
    stock = _validation_stock(stock)

    # Create the product after all validations pass.
    product = {
        "code": code,
        "name": name,
        "price": price,
        "stock": stock,
    }

    # Save the product in memory.
    products.append(product)

    # Save the updated products list in the JSON file.
    save_products(products)


# Deletes a product using its code.
def delete_product(products, code):
    # Search for the product with the requested code.
    convert_code = int(code)
    result = list(filter(
        lambda product: product["code"] == convert_code,
        products
    ))
    # If the product does not exist, raise an error.
    if not result:
        raise ValueError("Product not found")
    # Remove the product found from the list.
    products.remove(result[0])
    # Save the updated products list in the JSON file.
    save_products(products)