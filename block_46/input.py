from block_46.services import (
    register_product_from_text,
    search_product,
    increase_product_stock,
    decrease_product_stock,
)


def main():
    products = {}

    while True:
        print("\n===== PRODUCT MANAGEMENT =====")
        print("1. Register product")
        print("2. Consult stock")
        print("3. Increase stock")
        print("4. Decrease stock")
        print("5. Exit")

        option = input("Select an option: ").strip()

        try:
            if option == "1":
                text = input(
                    "Enter product (A123,CPU,15): "
                ).strip()

                register_product_from_text(products, text)

                print("Product registered successfully.")

            elif option == "2":
                code = input("Enter product code: ").strip()

                product = search_product(products, code)

                print(f"Product: {product.name}")
                print(f"Stock: {product.consult_stock()}")

            elif option == "3":
                code = input("Enter product code: ").strip()
                quantity = int(input("Quantity to add: "))

                increase_product_stock(products, code, quantity)

                print("Stock increased successfully.")

            elif option == "4":
                code = input("Enter product code: ").strip()
                quantity = int(input("Quantity to remove: "))

                decrease_product_stock(products, code, quantity)

                print("Stock decreased successfully.")

            elif option == "5":
                print("Goodbye.")
                break

            else:
                print("Invalid option.")

        except (ValueError, IndexError) as error:
            print(f"ERROR: {error}")


if __name__ == "__main__":
    main()