# for i in range(1,4):
#     for j in range(1,3):
#         print(j)

# # Global counter that persists across all rounds
# numbers_entered = 0

# # The for loop controls the fixed number of rounds (3 total)
# for i in range(1,4):

#     # The while loop handles dynamic input within each round
#     # It continues until the user enters 0
#     while True:
#         num = int(input("Enter a number (it will end when you enter the number 0):"))
        
#         # Exit condition for the current round
#         if num == 0:
#             break  # Leaves the while loop but not the for loop
        
#         # Count valid inputs (non-zero numbers)
#         numbers_entered += 1

# # Final result after all rounds are completed    
# print(f'The number of numbers entered was: {numbers_entered}')


# #a global counter, which is updated on each pass
# number_accumulator = 0

# #The while loop controls when the system will close
# while True:
#     num = int(input("Enter a number (it stops when the accumulated number exceeds 50):"))

    
#     #for loop iterates through the number number and adds it to the accumulator
#     for i in range(num):
#         number_accumulator += 1
#         print(number_accumulator)

#     #The exit condition is met when the number accumulator exceeds 50.
#     if number_accumulator > 50:
#         break

    

# #We print the accumulator and a check that we exited the loop
# print("You've broken out of the loop")
# print(f'The accumulated numbers were: {number_accumulator}')



# # Global state variables used throughout the program
# larger_number = None

# average_numbers = 0
# complete_cycles = 0

# #The while loop controls when the system will close
# while True:
#     number = int(input("Enter a number: "))


#     # Reset the sum for the current cycle
#     sum_numbers = 0


#     # Process N numbers for this cycle 
#     # For each number, we add it to the variable sum_large. 
#     for i in range(number):

#         another_number = int(input("Enter another number: "))
#         sum_numbers += another_number
        
#         # Update the global maximum if the new number is larger
#         if larger_number is None or larger_number < another_number:
#             larger_number = another_number
    

#     # Calculate the average for the current cycle
#     average_numbers = sum_numbers / number
    
#     #Count completed cycles (including the one that may trigger exit)
#     complete_cycles += 1
    

#     #Exit condition
#     if average_numbers > 50:
#         break

# print(f'The large number is: {larger_number}')


# # Global state variables that persist across all cycles
# valid_numbers = 0            # Total count of valid (non-negative) numbers entered
# last_valid_number = 0        # Total count of valid (non-negative) numbers entered
# sum_numbers = 0              # Accumulates the sum of all valid numbers



# #The while loop controls when the system will close
# while True:
    
#     #Process 5 numbers for this cycle
#     for i in range(5):
        
#         number = int(input("Enter 5 numbers (If the sum of number valid is max than 100, " \
#         "the program ends): "))
        
#         # Ignore negative numbers (they do not affect state)
#         if number < 0:
#             continue
        
#         # Update global state using only valid numbers
#         sum_numbers += number
#         last_valid_number = number
#         valid_numbers += 1
    
#     # Global exit condition evaluated only by the while loop
#     if sum_numbers > 100:
#         break


# print(f'The last valid number is: {last_valid_number}')
# print(f'The number of valid numbers are: {valid_numbers}')


#The global variables and flags 
# three_to_last = None           #variable that stores the third-to-last
# penultimate = None             #variable that stores the second-to-last number
# restricted_status = False      #flag that activates a special mode
# exit_condition = False         #flag that triggers the exit condition of the for loop

# count_odd = 0                  #odd number counter


# # The while loop controls when the system will close
# while True:


#     Process 3 numbers for this cycle
#     for i in range(3):

#         numbers = int(input("Enter to number (If the sequence is " \
#         "even odd even, the program ends): "))

#         for loop exit condition trigger
#         if numbers < 0 and restricted_status:
#             exit_condition = True
#             continue 

#         Ignore negative numbers if the special condition is not activated.
#         if numbers < 0:
#             continue
        

#         The detection of the sequence to activate restricted mode
#         if three_to_last is not None and penultimate is not None:
#             if three_to_last % 2 == 0 and penultimate % 2 == 1 and numbers % 2 == 0:
#                 restricted_status = True

#           Once the condition is activated, even numbers are 
#         ignored and odd numbers are counted.
#         if restricted_status:
#             if numbers % 2 == 0:
#                 continue
#             else:
#                 count_odd += 1
        
#         Update global state using only valid numbers
#         three_to_last = penultimate
#         penultimate = numbers
    

#     Global exit condition evaluated only by the while loop
#     if exit_condition:
#         break


# #The global variables and flags 
# all_numbers = 0           # accumulate valid numbers

# max_number = None            # variable for the largest number
# penultimate = None           # variable that stores the second-to-last number
# exit_condition = False       # Variable used to exit the for loop and terminate the program


# # The while loop controls when the system will close
# while True:
    
#     num = int(input("Enter any number: "))
    
#     # The loop iterates through N numbers
#     for i in range(num):
        
#         # Special condition that exits the for loop without breaking it
#         if exit_condition: 
#             continue 

#         another_num = int(input("Enter another number (If two identical " \
#         "numbers appear, the program ends): "))
        
#         # The detection of the sequence to activate special condition
#         if penultimate == another_num:
#             exit_condition = True
#             continue
        
#         # Activation and assignment of the maximum number
#         if max_number is None or max_number < another_num:
#             max_number = another_num

#         # Update global state using only valid numbers
#         penultimate = another_num
#         all_numbers += 1

#     # Global exit condition evaluated only by the while loop
#     if exit_condition:
#         break

# # Variables that persist across the entire execution
# count_odd = 0             # Counts valid odd numbers in restricted mode
# valid_nums = 0            # Counts valid numbers in restricted mode
# count_ignorenum = 0       # Counts ignored numberss in restricted mode


# max_num = None            # Stores the largest valid number entered
# exit_program = False      # Signals when the system must terminate
# restricted_mode = False   # Indicates whether restricted mode is active


# # The while loop controls the lifetime of the system
# while True:


#     # Counter used to evaluate the current block of 4 numbers
#     # It resets every cycle because activation depends only on this block
#     more_than = 0 


#     # Each cycle processes exactly 4 numbers
#     for i in range(4):


#         num = int(input("Enter any number (if all 4 numbers is greater than ten, the " \
#         "program ends): "))


#         # Exit condition detection
#         # we signal termination (but do not break the for loop).
#         if num < 0:
#             if restricted_mode:
#                 exit_program = True
#             continue


#         # --- Block evaluation logic ---
#         # Count how many numbers in this cycle are greater than 10.
#         # This determines whether restricted mode activates.
#         if num > 10:
#             more_than += 1


#         # --- Block evaluation logic ---
#         # Count how many numbers in this cycle are greater than 10.
#         # This determines whether restricted mode activates.
#         if restricted_mode:
#             if num % 2 == 0:
#                 count_ignorenum += 1
#                 continue
#             else:
#                 count_odd += 1
        

#         # Maximum tracking
#         if max_num is None or max_num < num:
#             max_num = num

#         # Count valid processed numbers
#         valid_nums += 1
    


#     # State activation
#     if more_than == 4:
#             restricted_mode = True

#     # Global termination decision
#     if exit_program:
#         break



# # Execution summary
# print("Valid numbers:", valid_nums)
# print("Ignored numbers:", count_ignorenum)
# print("Odd numbers in restricted mode:", count_odd)
# print("Max valid number:", max_num)


# # Variables that persist across the entire execution
# couples_generated = 0
# equals = 0

# # The first loop and second loop 
# for i in range (1,5):
#     for j in range (1,5):
        
#         # When comparing variables, if they are equal, 1 is added to the counter.
#         if i == j:
#             equals += 1
        
#         # Print all possible pairs
#         print (f'all possible pairs is: {i,j}')

#         # Counter of generated pairs
#         couples_generated += 1


# # Variables that are outside the loops
# larger_numbers = 0
# smaller_numbers = 0

# # Inner and outer loops that run from 1 to 6
# for i in range (1,7):
#     for j in range (1,7):

#         # Variable comparator, if i is less than j, one is added to smaller_number
#         if i < j:
#             smaller_numbers += 1
        
#         # Variable comparator, if i is greater than j, one is added to larger_numbers
#         if i > j:
#             larger_numbers += 1


# # Variables that are outside the loops
# iteration_count = 0
# count_par = 0

# # The first loop goes from 1 to 8
# # the second loop goes from 1 to the current positiond and i
# for i in range(1,8):
#     for j in range(1, i+1):

#         # If the sum of i, j is even, add one to the counter.
#         if (i+j) % 2 == 0:
#             count_par += 1
        
#         #Counter the iteration
#         iteration_count += 1


# # The global variable
# multiples_seven = 0

# # Inner and outer loops that run from 1 to 10
# for i in range (1,11):
#     for j in range (1,11):
        
#         # If the sum of the squares of i and j is a multiple of seven, add one to the counter.
#         if (((i**2)+(j**2)) % 7) == 0:
#             multiples_seven += 1



# # The global variables
# valid_counter = 0

# # The first loop is for 3 rouds
# # The seconds loop is while, it breaks when a certain condition is met.
# for i in range (3):
#     while True:
#         num = int(input("Enter any number (If number is 0, the loop end): "))
        
#         # If condition is True break the loop if not add one to the counter
#         if num == 0:
#             break
#         else:
#             valid_counter += 1


# # The first loop is for 3 rouds
# # The seconds loop is while, it breaks when a certain condition is met.
# for i in range (4):
    
#     # Internal variable of the loop while
#     sum_num = 0
#     number_entered = 0

#     while True:
#         num = int(input("Enter any number (If the sum is greater than 50, The loops ends): "))
#         sum_num += num
#         number_entered += 1

#         # If condition is True break the loop
#         if sum_num > 50:
#             break


#     print(f'The number entered for round is {number_entered}')



# # Total processed numbers across all cycles
# count_num = 0

# # Fixed structure: 5 independent cycles
# for i in range(5):

#     # Previous number for consecutive comparison (per cycle)
#     penultimate_number = None

#     # Variable loop: ends when two consecutive numbers are equal
#     while True:

#         num = int(input(
#             "Enter any number (If two consecutive numbers are equal, the loop ends): "))
#         count_num += 1

#         if penultimate_number == num:
#             break

#         penultimate_number = num


# last_sum= 0
# sum_num = 0

# for i in range(4):
    
#     sum_num = last_sum /2 

#     while True:
#         num = int(input("Enter any number (The loop ends if the sum of number is" \
#                         " 40): "))
#         sum_num += num

#         if sum_num > 40:
#                 break

#     last_sum = sum_num
    
    

        




        







        
        

       














    

