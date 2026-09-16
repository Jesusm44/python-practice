# # from random import randint

# # incognite = randint(1, 10)
# # count_failure = 0
# # count_acerted = 0

# # game_on = True

# # while game_on:
# #     intent = int(input("Enter any number between 1 and 10: "))

# #     if intent != incognite:
# #         count_failure += 1
# #         print(f"Wrong! Failures: {count_failure}/3")
# #     else:
# #         count_acerted += 1
# #         print(f"Correct! Successes: {count_acerted}/3")
       
# #         incognite = randint(1, 10) 

# #     if count_acerted == 3:
# #         print("Congratulations, you passed the test!")
# #         game_on = False 

# #     if count_failure == 3:
# #         print("You have run out of attempts, you cannot continue.")
# #         game_on = False

# # CURRENT_YEAR = 2026
# # CURRENT_MONTH = 9
# # CURRENT_DAY = 15

# # def calculate_age(year, month, day):
# #     age = CURRENT_YEAR - year

# #     if CURRENT_MONTH < month or (CURRENT_MONTH == month and CURRENT_DAY < day):
# #         age -= 1 

# #     return age

# # print("---CALCULATE_AGE---")

# # year = int(input("Enter your birth year (e.g., 1995): "))
# # month = int(input("Enter your birth month (1-12): "))
# # day = int(input("Enter your birth day (1-31): "))

# # user_age = calculate_age(year, month, day)

# # print(f"\nYour current age is: {user_age} years old.")

# import datetime

# today: datetime.datetime = datetime.datetime.now()
# current_year: int = today.year
# current_month: int = today.month
# current_day: int = today.day

# def calculate_age(year, month, day) -> int:
#     if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
#         raise ValueError("ERROR: Year, month or day not valid")

#     if year not in range(1899, 2028):
#         raise ValueError("Year not valid")

#     if month not in range(1, 13):
#         raise ValueError("ERROR: Month not valid")

#     if day not in range(1, 32):
#         raise ValueError("ERROR: DAY not valid")

#     age: int = current_year - year

#     if current_month < month or (current_month == month and current_day < day):
#         age -= 1 

#     return age

# try:
#     year = int(input("Enter your birth year (e.g., 1995): "))
#     month = int(input("Enter your birth month (1-12): "))
#     day = int(input("Enter your birth day (1-31): "))
#     user_age = calculate_age(year, month, day)
#     print(f"\nYour current age is: {user_age} years old.")
# except ValueError as e:
#     print(f"\nExecution stopped: {e}")