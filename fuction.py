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


