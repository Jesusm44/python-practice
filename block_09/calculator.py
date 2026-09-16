def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not possible.")
    return a / b


