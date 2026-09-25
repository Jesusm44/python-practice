# Function that helps us:
# 1. Check that the stock is an integer.
# 2. Ensure the rule that stock cannot be less than 0 is met.
def stock_validation(stock) -> int:
    if not isinstance(stock, int):
        raise ValueError("The stock is invalid")

    if stock <= 0:
        raise ValueError("The stock cannot be less than 0")

    return stock

#This function helps us save the stock after validation; since there is no `main` method, exceptions are evaluated within the function itself, as this is a test.
def save_stock(stock) -> None:
    try:
        stock = stock_validation(stock=stock)
        print(f"The product stock is: {stock}")
    except ValueError as error:
        print(error)