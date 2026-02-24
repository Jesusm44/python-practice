# # Global state variables
# active_system = True     # Variable that initializes the activate system
# current_process = True     # Variable that initializes the internal process


# loop_completed = 0          # Completed loop counter

# # External loop that activates the system when true
# while active_system:
    
#     numbers_entered = 0         # Counter of entered numbers
#     current_process = True     # Variable that initializes the internal process

#     while current_process:

#         num = int(input("Enter a number (The program ends when you enter 0): ")) 
#         numbers_entered += 1
        
#         # If the number is equal to zero, current_process is false
#         if num == 0:
#             current_process = False


#     # Counter for each completed loop
#     loop_completed += 1
    

#     # If loop_completed is greater than or equal to three, active_system is false
#     if loop_completed >= 3:
#         active_system = False




# # Accumulates the total sum across all completed internal cycles
# global_state = 0         

# # Outer loop: keeps the overall system running 
# # until the accumulated global total reaches 100
# while  global_state < 100:
    
#     # Tracks the sum for the current internal cycle.
#     # It is reset at the start of each outer iteration
#     # to ensure each cycle is independent
#     internal_state = 0
    
#     # Inner loop: processes a single cycle.
#     # It continues until the internal total exceeds 30
#     while internal_state <= 30:

#         num = int(input("Enter a number (The loop ends if the " \
#                         "internal state exceeds 30): ")) 
        

#         # Ignore negative inputs without affecting the internal total
#         if num < 0:
#             continue
        
#         # Accumulate only valid (non-negative) inputs
#         # into the current cycle total
#         internal_state += num
    
#     # After completing one internal cycle,
#     # add its total to the global accumulated state
#     global_state += internal_state



# # Global variables
# activate = True            # Controls whether the system remains active.

# number_sought = 7          # Target value that terminates the entire system when found.


# # Outer loop: while this is True the program runs.
# while activate:
    
#     # Internal variable that handles the inner loop, This is 
#     # initialized with each new iteration of the outer loop.
#     internal = True
    
#     # Inner loop: While the loop is active, it will ask us for a 
#     # series of numbers indefinitely until we find the number to search for.
#     while internal:
#         num = int(input("Enter a number (The loop ends if " \
#                         "you find the indicated number.): ")) 
        
#         # If the searched number is found,
#         # terminate both the internal process and the entire system
#         if num == number_sought:
#             internal = False
#             activate = False




# # State flags controlling internal behavior and overall system termination
# activation = False        # Enables special filtering logic during an attempt
# system_active = True      # Controls whether the entire system should continue running

 
# attempts = 0              # Tracks how many full attempts have been executed

# number_found = 7          # Target value that terminates the system when found


# # Outer loop: controls the lifecycle of attempts (maximum 5)
# while attempts < 5:

#     errors = 5            # Tracks remaining allowed iterations for the current attempt


#     # Inner loop: runs while there are remaining errors in the current attempt
#     while errors > 0:

#         num = int(input("Enter a number (The loop ends if "
#                         "you find the indicated number.): "))


#         # When remaining errors reach 3, activate additional filtering logic
#         if errors == 3:
#             print("The number begins with S.")
#             activation = True
        
#         # Decrement error counter to guarantee progress toward loop termination
#         # This must occur before any continue to prevent infinite loops
#         errors -= 1             
        
#         # When activation is enabled, apply additional filtering rules:
#         # Ignore numbers greater than 7
#         # Ignore even numbers
#         if activation:
#             if num > 7:
#                 continue
#             if num % 2 == 0:
#                 continue 
        
#         # If the target number is found, deactivate the system
#         # and exit the inner loop immediately
#         if num == number_found:
#             system_active = False
#             break

        
#     # One full attempt has completed
#     attempts += 1
    
#     # If the system has been deactivated, exit the outer loop
#     if not system_active:
#         break




# # Flag that indicates whether the user explicitly requested to exit the system.
# exit_condition = False

# # Constants used in the internal logic of the system.
# number_found = 3 
# sum = 12
# mult = 36
# answer = "Love"

# # Number of pending tasks that must be completed.
# tasks = 4

# # Represents limited system energy (resource constraint).
# # The external loop depends on this value being greater than zero.
# system_activate = 6

# division = 15


# # OUTER LOOP — System remains active while energy is available.
# # This loop represents the lifetime of the system.
# while system_activate > 0:

#     # This flag controls whether the special task mode is activated
#     # during the current outer iteration.
#     tasks_activation = False

#     # INNER LOOP — Executes while there are pending tasks.
#     # Represents active processing of work.
#     while tasks > 0:

#         # User input for task processing.
#         number = int(input(" Enter a number greater than 0 but less than 5: "))

#         # Exit condition triggered directly by user.
#         # Break only terminates the inner loop.
#         if number == 0:
#             exit_condition = True
#             break 

#         # If the special number is found:
#         # - Activate special task mode
#         # - Reduce tasks
#         # - Consume system energy
#         if number == number_found:
#             tasks_activation = True
#             tasks -= 1
#             system_activate -= 1
#         else:
#             # Incorrect number:
#             # - Increase pending tasks (penalty)
#             # - Consume system energy
#             tasks += 1
#             system_activate -= 1
#             tasks_activation = False 


#         # If task count grows beyond threshold,
#         # an additional validation challenge is triggered.
#         if tasks > 6:
#             num_div = int(input("What number divided by 45 gives 3"))

#             if num_div == division:
#                 # Additional input if validation passes.
#                 number = int(input(" Enter a number greater than 0 but less than 5: "))
#                 tasks += 1
#                 system_activate -= 1
#             else:
#                 # If validation fails but special number is entered,
#                 # special mode may activate again.
#                 if number == number_found:
#                     tasks_activation = True
#                     tasks -= 1
#                     system_activate -= 1
                

#         # SPECIAL TASK MODE
#         # If activated, additional subtasks must be completed.
#         if tasks_activation:

#             print("You have found the special number, now you must multiply "
#                   "and add that number by certain numbers to complete the tasks")

#             special_num_one = int(input("Enter any number a second time: "))
#             special_num_two = int(input("Enter any number a third time: "))
#             special_word = input("What is the only thing stronger than hate?")

#             # Each correct subtask:
#             # - Reduces pending tasks
#             # - Consumes system energy
#             if special_num_one + number == sum:
#                 tasks -= 1
#                 system_activate -= 1
                
#             if special_num_two * special_num_one == mult:
#                 tasks -= 1
#                 system_activate -= 1
                
#             if special_word == answer:
#                 tasks -= 1
#                 system_activate -= 1


#     # OUTER TERMINATION CONDITION
#     # System shuts down if:
#     # - User requested exit
#     # - All tasks were completed
#     if exit_condition or tasks == 0:
#         system_activate = 0

    

    

    



        

            




        


    

        

        






        







