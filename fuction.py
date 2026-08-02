# def greet_person(x):
#     print("Hello",x)

# greet_person("Peter")


# def sum_two_numbers(x,y):
#     return x + y

# def subtract_two_numbers(x,y):
#     return x - y

# print(sum_two_numbers(5,6))


# def give_good_days(name):
#     print(f'Hello, {name}')


# give_good_days("Peter")
# give_good_days("Mirian")


# def personal_data(name, year):
#     print(f'Hello my name is {name} and I am {year} years old')

# personal_data("Lois", 24)
# personal_data(24,"lois")

# def area_rectangle(b,h):
#     return b * h

# print(f'The area of a rectangle is {area_rectangle(5,6)}')
# print(f'The area of a rectangle is {area_rectangle(5,6,7,8)}') #Error lo pedia el ejercicio.


# def data_test(a,b,c):

#     return a / b + c

# print(f'The perimeter is: {data_test(7,15,8)}')
# print(f'The perimeter is: {data_test(8,15,7)}')


# a = input("Enter data: ")
# b = input("Enter a second piece of information: ")
# c = input("Enter a third piece of data: ")

# def data_testing(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# data_testing(a,b,c)


# def one_data_sum():
#     return 1 + 2 + 3

# print(one_data_sum())


# def two_data_sum(a,b,c):
#     return a + b + c

# print(two_data_sum(10,20,5))


# def sum_two_data(a,b):
#     return a + b


# def sum_two_data_one(a,b):
#     print(a+b)


# result = sum_two_data(5,6)
# result_one = sum_two_data_one(10,5)

# print(result)
# print(result_one)


# def function_one(a,b,c):
#     return a + b + c

# print(function_one(5,6,41))

# result = function_one(5,6,41)

# print(f'the perimeter of the scalene triangle: {result}')


# def function_with(a, b, c):
#     return a + b + c

# a = 0
# b = 0
# c = 0

# for i in range(3):
#     data = int(input("enter some data: "))

#     if i == 0:
#         a = data
#     elif i == 1:
#         b = data
#     else:
#         c = data

# result = function_with(a,b,c)

# print(result)

# def multiply(a,b):
#     result =  a * b
#     return result

# def division(a,b):
#     if a == 0:
#         print("Error: Cannot divide by zero.")
#     else:
#         result = a / b
#         return result

# def total_addition(a,b,c,d,e):
#     total_addition = a + b + c + d + e
#     return total_addition


# print(total_addition(1, 85, 16,25,30))
# print(division(1,5))

# def triangle_area(b,h):
#     result = (b * h) / 2
#     return result



# while True:
#     if area<= 25:
#         print("The area of this triangle does not meet the requirements.")
#         break
#     else:
#         print("The area of this triangle meets the requirements.")
#         break

# print(triangle_area(10,2))
# print(triangle_area(20,8))
# print(triangle_area(20.3,8.5))

# def results():
#     return 50

# def subtraction():
#     result = results()
#     return result - 21

# def addition():
#     final_result = subtraction() + 21
#     print(final_result)

# addition()


# def division(a,b):

#     if b == 0: 
#         print ("ERROR; YOU CANNOT DIVIDE BY 0")
#     else:
#         operation_result= a / b
#         return operation_result

# def addition(a,b):

#     operation_result = a + b
#     return operation_result

# def subtraction(a,b):

#     operation_result = a - b 
#     return operation_result

# def power(a):
#     operation_result = a ** 2
#     return operation_result


# radius = 7
# base = 5

# def area_triangle(h):

#     result_area = (base*h) / 2
#     return result_area

# def area_circle():
#     pi = 3.1416

#     result_area = pi * (radius**2)
#     return result_area


# print(area_circle())
# print(area_triangle(7))



# global_variable = 10

# def division_one(a):

#     if a == 0:
#         print("ERROR")
#     else:
#         result_divison = global_variable / a
#     return result_divison

# def division_two(a,b):

#     if b == 0:
#         print("ERROR")
#     else:
#         result_division = a / b
#     return result_division

# print(division_one(7))
# print(division_two(5,8))


# initial_value = 58

# def substraction_value(a):
#     global initial_value

#     initial_value  = initial_value - a
#     return initial_value

# def sum_value(a):
#     global initial_value

#     initial_value = initial_value + a
#     return initial_value

# def substraction_value_one(a):
#     global initial_value

#     initial_value = a - initial_value
#     return initial_value

# print(substraction_value(5))
# print(sum_value(85))
# print(substraction_value_one(52))

# print(initial_value)

# def value():
#     return 20

# def substraction_value(a):
#     result_value = value() - a
#     return result_value

# def addition_value(a):
#     result_value = value() + a 
#     return result_value

# print(addition_value(21))
# print(substraction_value(9))
# print(value())

# final_names = []
# correct_names = []
# repeated_names = []
# registered_names= set()
# fail_names = []

# def name_revision(name, registered_names, correct_names, repeated_names):

#     if name == "":
#         print("ERROR: Empty name")
#         return

#     if name in registered_names:
#         repeated_names.append(name)
#     else:
#         registered_names.add(name)
#         correct_names.append(name)


# while True:

#     name = input("Enter a name(type 'exit' to finish): ")

#     if name.lower() == "exit":
#         break

#     name_revision(
#         name, 
#         registered_names,
#         correct_names,
#         repeated_names
#     )

# print("Correct names:", correct_names)
# print("Repeated names:", repeated_names)
# print("Registered names:", registered_names)

# def normal_name(name,correct_names):

#     if name == "":
#         print("ERROR: DENIED NAME")
#         return

#     if not name.isalpha():
#         print("ERROR: DENIED NAME")
#         return

#     correct_names.append(name)

# def revision_name(name,repeated_names, registered_names, final_names):

#     if name in registered_names:
#         repeated_names.append(name)
#     else:
#         registered_names.add(name)
#         final_names.append(name)


# while True:

#     name = input("Enter a name (type 'exit' to finish): ")

#     if name.lower() == "exit":
#         break

#     normal_name( name, correct_names)
#     revision_name(name,repeated_names,registered_names,final_names)



# print(correct_names)
# print(registered_names)
# print(final_names)

# money = 10
# food_order = None
# pickup = 0
# deposit = 0


# def bank_acc(name):
#     global deposit, pickup, food_order

#     if name == "":
#         print("Name ERROR")
#         return

#     if not name.isalpha():
#         print("ERROR: Invalid Name")
#         return

#     if deposit > 0:
#         deposit+= money
#     else:
#         print("ERROR: INVALID DEPOSIT")

#     if pickup > money:
#         print("ERROR: You do not have enough funds")
#         return
#     else:
#         print(f'Success deposit. Remaining balance{money}')

#     if food_order == "":
#         print("ERROR: The order is empty")
#         return
#     else:
#         print("WHAT THE HELL ARE YOU DOING ASKING FOR FOOD AT THE BANK?")


# available_balance = 20

# def deposit(new_deposit, available_balance):

#     if new_deposit < 0:
#         print("ERROR: The deposit cannot be 0 less")
#         return available_balance

#     available_balance += new_deposit
#     print("Successful deposit")
#     return available_balance

# def withdrawal(new_withdrawal, available_balance):

#     if new_withdrawal < 0:
#         print("ERROR: The withdraw cannot be 0 less")
#         return available_balance

#     if new_withdrawal > available_balance:
#         print("You cannot withdraw an amount greater than your balance.")
#         return available_balance 

#     available_balance -= new_withdrawal
#     print("Withdrawal successfully completed")
#     return available_balance

# def information(available_balance):
#     print(f'The available balance is: {available_balance}')


# while True:

#     option = input(
#         "1. Deposit\n"
#         "2. Withdrawal\n"
#         "3. Show balance\n"
#         "4. Exit\n"
#         "Choose an option: "
#     )

#     if option == "1":
#         new_deposit = float(input("Enter the amount to deposit: "))

#         available_balance = deposit(new_deposit,available_balance)

#     elif option =="2":
#         new_withdrawal = float(input("Enter a new withdrawal amount: "))
#         available_balance = withdrawal(new_withdrawal, available_balance)

#     elif option == "3":
#         information(available_balance)

#     elif option == "4":
#         print("Logging out... Session closed.")
#         break


available_balance = 20

def validation(a):

    if a < 0:
        print("The amount must be greater than 0.")
        return False
    else:
        return True

def deposit(new_deposit, available_balance):

    if validation(new_deposit):
        available_balance += new_deposit
        print("Successful deposit")
        return available_balance

def withdrawal(new_withdrawal, available_balance):

    if validation(new_withdrawal):
        if new_withdrawal > available_balance:
            print("You cannot withdraw an amount greater than your balance.")
            return available_balance 

        available_balance -= new_withdrawal
        print("Withdrawal successfully completed")
        return available_balance

def information(available_balance):
    print(f'The available balance is: {available_balance}')

while True:

    option = input(
        "1. Deposit\n"
        "2. Withdrawal\n"
        "3. Show balance\n"
        "4. Exit\n"
        "Choose an option: "
    )

    if option == "1":
        new_deposit = float(input("Enter the amount to deposit: "))

        available_balance = deposit(new_deposit,available_balance)

    elif option =="2":
        new_withdrawal = float(input("Enter a new withdrawal amount: "))
        available_balance = withdrawal(new_withdrawal, available_balance)

    elif option == "3":
        information(available_balance)

    elif option == "4":
        print("Logging out... Session closed.")
        break















