# simulation_group = [5,10,3,0]
# new_list = []

# for i in simulation_group:
#     if i == 0:
#         break
#     else:
#         new_list.append(i)
          
# print(new_list)


# first_list = [3,7,12,5,20]
# second_list = []

# for i in first_list:

#     if i > 10:
#         second_list.append(i)

# print(second_list)


# normal_list = [1,2,3,4]
# list_squares = []

# for i in normal_list:

#     squares = i**2
#     list_squares.append(squares)

# print(list_squares)


# normal_list = [10,20,5,30,25]

# larger_number = normal_list [0]
# minus_number = normal_list [0]

# for i in normal_list:
#     if larger_number < i:
#         larger_number = i

# print(larger_number)


# normal_list = [10,20,5,30,25]
# minus_number = normal_list [0]
# for i in normal_list:

#     if minus_number > i:
#         minus_number = i

# print(minus_number)


# numbers = [3,7,12,5,20]
# count_larger = 0

# for i in numbers:
#     if i > 10:
#         count_larger += 1

# print(count_larger)


# numbers = [10,20,30]

# div = len(numbers)
# sum_numbers = 0

# for i in numbers:
#     sum_numbers += i

# average = sum_numbers / div

# print(average)

# numbers = [4,9,2,15,6,20]
# largest_ten = []

# largest_number = numbers[0]
# minus_number = numbers[0]
# count_even = 0

# for i in numbers:

#     if largest_number < i:
#         largest_number = i

#     if minus_number > i:
#         minus_number = i

#     if i % 2 == 0:
#         count_even += 1
    
#     if i > 10:
#         largest_ten.append(i)


# print(largest_number)
# print(minus_number)
# print(count_odd)
# print(largest_ten)


# numbers = [3,7,2,7]

# found = False

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
        
#         if i != j and numbers[i] == numbers[j]:
#             found = True
#             break
    
#     if found:
#         break

# print(found)
            
# numbers = [42, 7, 89, 13, 65, 28, 91, 3, 54, 76]

# for i in numbers:
#     for j in numbers:
#         print(i,j)


# numbers = [42, 7, 89, 13, 65, 28, 91, 3, 54, 76]

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         print(numbers[i],numbers[j])


# numbers = [42, 7, 89, 13, 65, 28, 91, 3, 54, 76]

# for i in numbers:
    
#     count = 0  # contador PARA ESTE número
    
#     for j in numbers:
#         if j > i:
#             count += 1

#     print(f"{i} → {count}")


# numbers = [42, 7, 89, 13, 65, 28, 91, 3, 54, 76]

# for i in range(len(numbers)):
#     for j in range(i+i,len(numbers)):
#         if numbers[i]+numbers[j] == 100:
#             print(numbers[i], numbers[j])


# new_list = []
# clean_list = []
# accumulation = 0
# count = 0
# pair = []

# while True:

#     numbers = input("Enter numbers for a list; entering finish closes the list: ")
    
#     if numbers == "finish":
#         break
#     else:
#         numbers = int(numbers)
    
#     new_list.append(numbers)

# for i in new_list:

#     if i > 0:
#         x = i * 2
#         clean_list.append(x)

# for i in clean_list:
#     accumulation += i


# if clean_list:
#     average = accumulation / len(clean_list)
# else:
#     print("ERROR")

# for i in clean_list:

#     if i > average:
#         count += 1


# for i in range(len(clean_list)):
#     for j in range(i+1, len(clean_list)):

#         if clean_list [i] + clean_list[j] == 10:
#             pair.append((clean_list[i],clean_list[j]))


# print(f'First list: {new_list}')
# print(f'Clean list: {clean_list}')
# print(f'The average is: {average}')
# print(f'The count is: {count}')
# print(f'Pairs that add up to 10: {pair}')