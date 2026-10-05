# Import the required functions from the service module.
from service import search_product, show_products
from save import delete_product, save_product, delete_product


def main():
    # Control variable used to keep the program running.
    run_program = True

    # List where products will be stored during program execution.
    products = []

    # The menu keeps running while run_program is True.
    while run_program:
        print("""
   Menu options
-------------------
1. Save product
2. Search product
3. Show products
4. Delete product
5. Exit""")

        # Ask the user to choose an option from the menu.
        option = int(input("Choose an option: "))

        # Option 1: save a new product.
        if option == 1:
            # Ask the user for the product information.
            code = input("Write the product code: ")
            name = input("Write the product name: ")
            price = input("Write the price: ")
            stock = input("Write the stock: ")

            try:
                # Try to save the product in the products list.
                save_product(products,code,name,price,stock)
                # This message is shown only if no exception occur.
                print("File saved successfully.")

            # Handle errors related to invalid values.
            except ValueError as error:
                print(error)
            # Handle errors related to invalid data types.
            except TypeError as type_error:
                print(type_error)

        # Option 2: search for a product by its code.
        elif option == 2:
            code = input("Write the product code: ")

            try:
                # Search for the product and store the returned result.
                product = search_product(products, code)

                # Display the product that was found.
                print(f"Product found: {product}")

            # Handle errors if the product cannot be found.
            except ValueError as error:
                print(error)

        # Option 3: show all products.
        elif option == 3:
            # Get the products from the show_products function.
            product = show_products(products)

            # Display the returned result.
            print(product)

        # Option 4: delete a product by its code.
        elif option == 4:
            code = input("Write the product code: ")

            try:
                # Try to delete the product from the list.
                delete_product(products, code)

                # Display a confirmation message if deletion succeeds.
                print("Product deleted successfully")

            # Handle errors if the product cannot be deleted.
            except ValueError as error:
                print(error)

        # Option 5: exit the program.
        elif option == 5:
            print("Exiting the program")

            # Change the control variable to stop the while loop.
            run_program = False

        # Handle menu options that do not exist.
        else:
            print("ERROR: Invalid option")


# Run main() only when this file is executed directly.
# This block does not run when the file is imported as a module.
if __name__ == "__main__":
    main()