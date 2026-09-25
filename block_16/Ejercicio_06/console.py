from service import  save_product, search_product, show_products, delete_product

def main():
    run_progam = True
    products = []

    while run_progam:
        print("""
   Menu options
-------------------
1. Save product
2. Shearch product
3. Show products
4. Delete product
5. Exit""")
        option = int(input("Chose a option: "))

        if option == 1:
            code = input("Write the product code: ")
            name= input("Write the product name: ")
            price = input("Write the price: ")
            stock = input("Write the stock: ")
            try:
                save_product(products, code, name, price, stock)
                print("Product saved successfully")
            except ValueError as error:
                print(error)
            except TypeError as tyerror:
                print(tyerror)
        elif option == 2:
            code = input("Write the product code: ")
            try:
                product = search_product(products,code)
                print(f'Product found: {product}')
            except ValueError as error:
                print(error)
        elif option == 3:
            product = show_products(products)
            print(product)
        elif option == 4:
            code = input("Write the product code: ")
            try:
                delete_product(products,code)
                print("deleted code")
            except ValueError as error:
                print(error)
        elif option == 5:
            print("Exiting the program")
            run_progam = False
        else:
            print("ERROR: Invalid option")


if __name__ == "__main__":
    main()


