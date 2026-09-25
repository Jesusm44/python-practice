from domain import (
    _validation_code,
    _validation_name,
    _validation_price,
    _validation_stock
)

# Validates the product data and saves the product in the list.
def save_product(products: list, code, name, price, stock):
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
        "stock": stock
    }
    # Save the product in the products list.
    products.append(product)
    return products

# Searches for a product using its code.
def search_product(products, code):
    # Filter the products that have the requested code.
    convert_code = int(code)
    result = list(filter(
        lambda product: product["code"] == convert_code,
        products
    ))

    # If no product was found, raise an error.
    if not result:
        raise ValueError("Product not found")

    # Return the product found.
    return result[0]

# Returns all saved products.
def show_products(products):
    return products

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