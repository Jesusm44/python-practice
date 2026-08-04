# porcentage_vat = 0.15

# def vat(base_price, porcentage_vat):
    
#     vat_calculate = base_price * porcentage_vat

#     total_pay = vat_calculate + base_price

#     return total_pay

# print(f'The total price to pay is: {vat(1500, porcentage_vat, )}')


# def personal_information(name, age, city):
#     return f'Your details are: your name are: {name}, your age are: {age}, your city are: {city}'


# while True:
    # print("Enter your name, your age, and your city. If you type exit, the program will close.")
    
    # name = input("Enter your name: ").capitalize()

    # if name == "Exit":
    #     print("Thanks, come again soon!")
    #     break

    # age = int(input("Enter your age: "))
    # city = input("enter your city: ").capitalize()

# def area_square(base,high):

#     if base  == 0 or high == 0:
#         print ("ERROR: IT IS NOT POSSIBLE TO CALCULATE THE AREA")
#     else:
#         area = base * high
#         print(f'The are of square is: {area}')

# area_square(100000,1000)

# grades = [18,15,20,12,19,14,17]

# def average_calculate(grades):
#     count_grade  = 0
#     total_grade = 0

#     for i in grades:
#         total_grade += i
#         count_grade += 1

#     average = total_grade / count_grade

#     return average

# def higher_grade(grades):
#     highest_grade = grades[0]

#     for i in grades:
#         if i > highest_grade:
#             highest_grade = i

#     return highest_grade

# def lower_grade(grades):
#     lowest_grade = grades[0]

#     for i in grades:
#         if i < lowest_grade:
#             lowest_grade = i

#     return lowest_grade

# def approval_counter(grades):
#     approval_count = 0

#     for i in grades:
#         if i >= 10:
#             approval_count += 1

#     return approval_count

# def fail_counter(grades):
#     fail_count = 0

#     for i in grades:
#         if i < 10:
#             fail_count += 1

#     return fail_count

# def grade_report(grades):
#     return f"""
#     The average grade is: {average_calculate(grades)}
#     The highest grade is: {higher_grade(grades)}
#     The lower grade is: {lower_grade(grades)}
#     The approved grades are: {approval_counter(grades)}
#     The failed grades are: {fail_counter(grades)}"""

# print(grade_report(grades))


# products = [
#     {"id": 101, "nombre": "Laptop", "precio": 950},
#     {"id": 102, "nombre": "Mouse", "precio": 20},
#     {"id": 103, "nombre": "Monitor", "precio": 280},
#     {"id": 104, "nombre": "Teclado", "precio": 45}
# ]

# def expensive_product(products):
#     most_expensive = None

#     for product in products:
#         price = product["precio"]
        

#         if most_expensive is None or price > most_expensive:
#             most_expensive = price

#     return most_expensive

# def cheapest_product(products):
#     cheap_product = None

#     for product in products:
#         price = product["precio"]

#         if cheap_product is None or cheap_product > price:
#             cheap_product = price

#     return cheap_product

# def average_price(products):
#     count_products = 0
#     total_price = 0

#     for product in products:
#         price = product["precio"]

#         count_products += 1
#         total_price += price

#     average_prices = total_price / count_products

#     return average_prices

# def search_id(products):
#        while True:
#         print("Search for the product by ID; if it's correct, the product will appear. Enter 0 to exit" "\n")

#         search = int(input("Enter the ID; it can only be numbers: "))

#         if search == 0:
#             break
#         else:
#             for product in products:
#                 if product["id"] == search:
#                     return product
                
#             return "ERROR ID NOT FOUND"

# def show_results(products):

#     return f"""
#         The most expensive product is: {expensive_product(products)}
#         The cheapest product is: {cheapest_product(products)}
#         The average price is: {average_price(products)}
#         Your products is: {search_id(products)}"""

# print(show_results(products))

# def valid_percentage(percentage):

#     if percentage > 100 or percentage <= 0:
#         return False
#     else:
#         return True

# def discounted_products(product_price, percentage):

#     discounts = (percentage /  100) * product_price
#     total_pay = product_price - discounts

#     return total_pay

# while True:
    # option = input("Enter the options: \n"
    #     "1. Total to pay, with the discount \n" \
    #     "2. Exit the app : "
    # )

    # if option == "1":
    #     product_price = int(input("Enter the product price: "))
    #     percentage = int(input("Enter the percentage of the product: "))
    #     if valid_percentage(percentage):
    #         print(discounted_products(product_price,percentage))
    #     else:
    #         print("ERROR: Invalid percentage")
    #         break
    # elif option == "2":
    #     print("Closing the app...")
    #     break
    # else:
    #     print("ERROR: Invalid option")
    #     break

estudiantes = [
    {
        "id": 1,
        "nombre": "Ana",
        "edad": 19,
        "promedio": 17
    },
    {
        "id": 2,
        "nombre": "Luis",
        "edad": 22,
        "promedio": 14
    },
    {
        "id": 3,
        "nombre": "María",
        "edad": 20,
        "promedio": 19
    }
]















