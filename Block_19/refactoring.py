def read_product_data() -> tuple[str, str, int]:
    code: str = input("Code: ")
    name: str = input("Name: ")
    stock = int(input("Stock: "))
    return code, name, stock

def validate(code, name, stock)  -> dict[str, str | int]:
    if stock < 0:
        print("Invalid stock.")
        raise ValueError("Invalid stock.")

    product:dict[str, str |  int] = {
        "code" : code,
        "name" : name,
        "stock" : stock,
    }
    print("Register product,")
    return product

def show_product(product) -> None:
    print(f"The product is: {product}")

def register_product() -> None:
    code, name, stock = read_product_data()
    product: dict[str, str | int] = validate(code,name,stock)
    show_product(product=product)