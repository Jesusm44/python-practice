from .input import enter_product, options, chose,enter_code
from .domain import create_product,valid_code
from .services import search_product,register_product
from utilitys.json_io import save_inventory, load_inventory


inventory= {}

def main():
    activate_inventory = True
    while activate_inventory:
        try:
            print(options())
            option: int = chose()
            if option == 1:
                name, price, stock = enter_product()
                code = enter_code()
                valid_code(inventory,code)
                product = create_product(
                    name = name,
                    price = price,
                    stock= stock
                )
                register_product(inventory,code,product)
                print("Created product")
            elif option == 2:
                save_inventory(inventory)
            elif option == 3:
                code = enter_code()
                product = search_product(
                    inventory=inventory,
                    code = code
                )
                print(product)
            elif option == 4:
                loaded_inventory = load_inventory()
                inventory.clear()
                inventory.update(loaded_inventory)
                print("Inventory loaded.")
            elif option == 5:
                activate_inventory = False
        except ValueError as error:
            print(error)

if __name__ == "__main__":
    main()