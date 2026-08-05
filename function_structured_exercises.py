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
#     option = input("Enter the options: \n"
#         "1. Total to pay, with the discount \n" \
#         "2. Exit the app : "
#     )

#     if option == "1":
#         product_price = int(input("Enter the product price: "))
#         percentage = int(input("Enter the percentage of the product: "))
#         if valid_percentage(percentage):
#             print(discounted_products(product_price,percentage))
#         else:
#             print("ERROR: Invalid percentage")
#             break
#     elif option == "2":
#         print("Closing the app...")
#         break
#     else:
#         print("ERROR: Invalid option")
#         break


# students = [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 19,
#         "average": 17
#     },
#     {
#         "id": 2,
#         "name": "Luis",
#         "age": 22,
#         "average": 14
#     },
#     {
#         "id": 3,
#         "name": "María",
#         "age": 20,
#         "average": 19
#     }
# ]

# def search_id(students):
#     search = int(input("Enter the ID you are looking for: "))

#     for student in students:

#         if student["id"] == search:
#             return student
 
#     return False

# def calculate_general_averages(students):
#     sum_average = 0
#     count_general_average = 0
    
#     for student in students:
#         count_general_average += student["average"]
#         sum_average += 1

#     total_general_average = count_general_average / sum_average
#     return total_general_average

# def best_average(students):
#     average_best = None

#     for student in students:
#         if average_best is None or student["average"] > average_best:
#             average_best = student["average"]
#     return average_best

# def worst_average(students):
#     average_worst = None

#     for student in students:
#         if average_worst is None or student["average"] < average_worst:
#             average_worst = student["average"]
#     return average_worst

# def adults(students):
#     count_adults = 0
    
#     for student in students:
#         if student["age"] >= 18:
#             count_adults +=  1
#     return count_adults 

# def approved_students(students):
#     count_approved = 0

#     for student in students:
#         if student["average"] >= 10:
#             count_approved += 1
#     return count_approved

# def update_average(students):
#     student = search_id(students)

#     if student:
#         change_average = int(input("Enter the average you want to change: "))

#         if change_average > 20 or change_average < 0:
#             return "ERROR: Average are not allowed"
#         else:
#             student["average"] = change_average
#     else:
#         return "No student with that ID was found"

# def verify_student(students):
#     search_student = input("Enter the name of the student you are looking for: ")

#     for student in students:
#         if student["name"] == search_student:
#             return f'The student has been found {student["name"]}'
        
#     return "Student not fount"

# while True:

#     print("You choose options, to know what you want to do.")

#     options = input("Enter a number to choose the option you  want: \n" \
#         "1. Search id \n" \
#         "2. Calculate the overall averages \n"
#         "3. Find a better average \n"
#         "4. Find the lowest average \n" 
#         "5. Count adults \n"
#         "6. Count students who passed \n"
#         "7. Update a student's average \n"
#         "8. Check if a student exists \n"
#         "9. Exit the app \n" 
#         ": "
#     )

#     if options == "1":
#         print(f'The student found is: {search_id(students)}')
#     elif options == "2":
#         print(f'The calculation of averages is: {calculate_general_averages(students)}')
#     elif options == "3":
#         print(f'The best average is {best_average(students)}')
#     elif options == "4":
#         print(f'The worst average is: {worst_average(students)}')
#     elif options == "5":
#         print(f'The number of adults is: {adults(students)}')
#     elif options == "6":
#         print(f'Number of students passed: {approved_students(students)}')
#     elif options == "7":
#         print(f'Your update was successful: {update_average(students)}')
#     elif options == "8":
#         print(f'The verification is correct: {verify_student(students)}')
#     elif options == "9":
#         print("Exit the program...")
#         break
#     else:
#         print("ERROR: This option does not exist")

# def obtain_linear_equation_data():
#     a = int(input("Enter any number: "))
#     b = int(input("Enter any second number: "))
#     c = int(input("Enter any third number: "))

#     return a, b, c

# def validate_data_equation_linear():
    
#     a,b,c = obtain_linear_equation_data()

#     if a == 0:
#         if b == c:
#             print("The equation has infinite solutions (Identity).")
#         else:
#             print("The equation has no solution (Inconsistency).")
#         return None
    
#     return a, b, c

# def generation_of_results():
#     data = validate_data_equation_linear() 
    
#     if data is None:
#         return

#     a, b, c = data

#     result = (c - b) / a

#     return result 

# def show_results():
#     show = generation_of_results()
#     if show is not None:
#         print(f"The result of the function is: {show}")

# show_results()








