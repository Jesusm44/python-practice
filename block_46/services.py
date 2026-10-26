from block_46.products import Products

products = {}

def register_products(products, code, name, stock):
    if code not in products:
        products[code] = Products(code,name,stock)
        return products
    else:
        raise ValueError("The product is registered.")


def search_product(products,search_code):
    if search_code not in products:
        raise ValueError("The product is not available.")
    return products[search_code]


def increase_product_stock(products, code, quantity):
    find_code = search_product(products,code)
    find_code.add_stock(quantity)

def decrease_product_stock(products, code, quantity):
    find_code_reduce = search_product(products,code)
    find_code_reduce.reduce_stock(quantity)


def register_product_from_text(products, text):
    product = Products.from_text(text)

    if product.code in products:
        raise ValueError("The product is already registered.")

    products[product.code] = product
