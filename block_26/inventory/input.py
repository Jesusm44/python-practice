from typing import LiteralString

def enter_code():
    code: str = input("Code: ")
    return code

def enter_product() -> tuple[str, float, int]:
    name: str = input("Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    return  name, price, stock

def options() -> LiteralString:
    return f"""
---OPTION---
1. Create product
2. Save product
3. Search product
4. Load product
5. Exit"""

def chose() -> int:
    option = int(input("Enter option: "))
    return option

