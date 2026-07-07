# basics
name = "Jesus"
age = 24
stature = 1.73
studie = True

# operators
# number_one = int(input("Give me a natural number: "))
# number_two = int(input("Give me a natural number: "))

# print(number_one + number_two)
# print(number_one - number_two)
# print(number_one * number_two)
# print(number_one ** number_two)
# print(number_one // number_two)

# enter_age = int(input("Enter your age: "))

# if enter_age >= 18:
#     print("You can come in")
# else:
#     print("You can't come in")

# enter_rating = float(input("Enter your grade:"))

# if 90 <= enter_rating <= 100:
#     print("Excelent; your rating is: " , enter_rating)
# elif 80 <= enter_rating <= 89:
#     print("Very Good; your rating is: " , enter_rating)
# elif 70 <= enter_rating <=79:
#     print("Good; your rating is: " , enter_rating)
# elif 60 <= enter_rating <= 69:
#     print("This is sufficient; your grade is: ", enter_rating)
# else:
#     print("You failed; your grade is: ", enter_rating)

# x = 0

# while x < 100:
#     x += 1
#     print(x)

# for i in range(1,101):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# total_sum = 0

# for i in range(101):
#     total_sum += i

# print(total_sum)


# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(1,11):
#     print("Multiplier table of the ", i)
#     for j in range(1,11):
#         print(f'{i} x {j} = {i*j}')
#     print()

# ten_numbers = [14, 87, 3, 56, 91, 28, 65, 10, 42, 79,3]

# print(f'The number in the fistr positions is: {ten_numbers[0]}')
# print(f'The number in the last position is: {ten_numbers[10]}')
# print(f'The length is: {len(ten_numbers)}')

# total_sum = 0
# average = 0
# larger = ten_numbers[0]
# smaller = ten_numbers[0]
# len_list=len(ten_numbers)
# previous_number = 0
# even_numbers = []
# unique_numbers = []

# for i in ten_numbers:
#     print(i, end= " ")
#     total_sum += i

#     if i > larger:
#         larger = i
#     if i < smaller:
#         smaller = i

#     if i % 2 == 0:
#         even_numbers.append(i)

#     if i  not in unique_numbers:
#         unique_numbers.append(i)
        
# print()

# average = total_sum/len_list

# print(f'The list average is: {average}')
# print(f'The total sum of the list is: {total_sum}')
# print(f'The largest number is: {larger}')
# print(f'The smaller number is: {smaller}')
# print(f'The even numbers in the list are: {even_numbers}')
# print(f'The unique numbers on the list are: {unique_numbers}')

# set_a = {"a","b","c","f","e","h"}
# set_b = {"b","a","b","c","f"}

# set_c = set_a | set_b
# set_d = set_a & set_b
# set_e = set_a - set_b

# print(set_c)
# print(set_d)
# print(set_e)

# ten_words = []
# no_repeat = set()


# for i in range(10):
#     words = str(input("Enter a word: "))

#     if words not in no_repeat:
#         ten_words.append(words)
#         no_repeat.add(words)
#     else:
#         continue

# print(ten_words)

# user = {
#     "name" : "Jesus",
#     "age" : 24,
#     "city" : "caracas",
#     "profession" : "developer"
# }
# for key, value in user.items():
#     print(key,value)


# if "venezuela" in user.values():
#     print("It exists")
# else:
#     print("It doesn't exist")

# print(user)

# def saludar(name):
#     print("Bienvenido", name)

# saludar("Valeria")

# def sum(a,b):
#     print(a + b)

# sum(5,6)


# def sum(c,d):
#     return c + d

# print(sum(7,15))

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(2))

# def larger_number(a,b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(larger_number(5,40))

# def average(a):
#     total_sum = 0

#     for i in a:
#         total_sum += i

#     promedy = total_sum / len(a)
    
#     return promedy

# list_num = [1,58,45,75,6,8,9,10,11,25]

# print(average(list_num))

# def vowel_counter(text):
#     count_vowel = 0

#     for i in text:
#         if i in "aeiou":
#             count_vowel += 1
    
#     return count_vowel

# print(vowel_counter("parallelepiped"))