def valid_product(name, price, stock):

    if not name.strip():
        raise ValueError("ERROR: Invalid Name.")
    if len(name) < 3:
        raise ValueError("ERROR: Empty name.")
    
    if price < 0:
        raise ValueError("ERROR: Price not valid.")

    if stock < 0:
        raise ValueError("ERROR: Invalid stock")

def valid_code(inventory, code):
    if code in inventory:
        raise ValueError("ERROR: The code cannot be duplicated.")

    if not code.isalnum():
        raise ValueError("ERROR: Code not valid.")

    return code
    
def create_product(name, price, stock):
    valid_product(name, price, stock)
    product = {
        "name": name,
        "price": price,
        "stock": stock
    }
    return product 

