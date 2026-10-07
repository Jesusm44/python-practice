from services import register_product,search_product
from domain import creat_product


inventory = {}

def input_code() -> str:
    code: str = input("Code: ")
    return code

def input_product() -> tuple[str, int, float]:
    name: str = input("Name: ")
    stock = int(input("Stock: "))
    price = float(input("Price: "))
    return name, stock, price

def show_menu():
    print(f"""
---OPTIONS---
1. Register product
2. Search product 
3. Exit """)

def main():
    activate_system = True
    while activate_system:
        show_menu()
        try:
            chose = int(input("Chose option: "))
            if chose == 1:
                name, stock, price = input_product()
                code = input_code()
                product = creat_product(name,stock, price)
                register_product(inventory, code, product)
                print("Product successfully registered")
            elif chose == 2:
                code = input_code()
                print(f"Find product: {search_product(inventory,code)}")
            elif chose == 3:
                print("Exit...")
                activate_system = False
            else:
                raise ValueError("The option does not exist.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()

print(inventory)

