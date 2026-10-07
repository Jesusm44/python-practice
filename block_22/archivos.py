import pathlib 

path: pathlib.Path = pathlib.Path(__file__).parent / "data" / "data.txt"

def write_products():
    with path.open("w", encoding="utf-8",) as file:
        file.write("Monitor\n")
        file.write("Mausepad\n")
        file.write("CPU\n")

def read_product():
    with path.open("r", encoding="utf-8",) as file:
        content = file.read()
    return content

write_products()
products = read_product()
print(products)

