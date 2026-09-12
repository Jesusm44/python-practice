from typing import Any

def validate_number(value) -> None :
    if not isinstance(value, int):
        print("NUMBER NOT FOUND")

def addition(a,b) -> Any:
    validate_number(a)
    validate_number(b)
    return a + b 

def subtraction(a,b) -> Any:
    validate_number(a)
    validate_number(b)
    return a - b
