# We define a class; this is an exception.
class StockInvalidError(Exception):
    pass

# We create the stock validation function, which includes the following:
#   1. If the stock is not an integer, it returns an error.
#   2. If the stock is less than 0, it returns an error;
#   otherwise, it returns the stock.
def validation_stock(stock: str) -> int:
    if not isinstance(stock, int):
        conver_stock = int(stock)
        if not isinstance(conver_stock, int):
            raise ValueError ("ERROR: The stock must be a whole number.")
        return conver_stock
    
    if stock < 0:
        raise StockInvalidError("ERROR: Stock cannot be a negative number.")

    return stock

# We create the `main` function, which is responsible for handling the previous functions; this is where we decide what to do if an error occurs.
def main() -> None:
    try:
        stock = input("Enter your stock: ")
        stock = validation_stock(stock)
        print("Stock successfully saved")
    except StockInvalidError as error:
        print(error)
    except ValueError as error:
        print(error)

# Condition that checks if we are on the main branch.
if __name__ == "__main__":
    main()