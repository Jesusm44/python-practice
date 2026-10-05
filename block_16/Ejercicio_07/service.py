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

