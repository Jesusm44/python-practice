inventory = {}
inventory_a = {}
inventory_b = {}

def product_register(inventory, code, product):
    if not code.isalnum():
        raise ValueError("ERROR: Invalid code")
    inventory[code] = product 

def search_product(inventory, code):
    return inventory.get(code)



