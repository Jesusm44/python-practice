def register_product(inventory, code, product):
    inventory[code] = product


def search_product(inventory, code):
    return inventory.get(code)