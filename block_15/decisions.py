from collections import Counter
from pathlib import Path
import datetime
import json
from typing import Literal
import random
import time

numbers = [1, 2, 3, 4, 5, 2, 6, 7, 3, 8, 9, 1, 4, 10, 5]
print(f'each number appears {Counter(numbers)}')

repeat_numbers = {}
for number in numbers:
    if number in repeat_numbers:
        repeat_numbers[number] += 1
    else:
        repeat_numbers[number] = 1

print(repeat_numbers)


today: datetime.date = datetime.date.today()
future: datetime.date = today + datetime.timedelta(days=90)
print(today,future)

def leap_year(year) -> Literal[29] | Literal[28]:
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return 29
    return 28

def months(month, year) -> Literal[29] | Literal[28] | Literal[31] | Literal[30]:
    if month < 1 or month > 12:
        raise ValueError("El mes debe estar entre 1 y 12")
    
    if month == 2:
        two_month: Literal[29] | Literal[28] = leap_year(year)
        return two_month
    elif month in (1, 3, 5, 7, 8,10, 12):
        return 31
    
    else:
        return 30

def days_ad(day, month, year, count_day):
    while count_day > 0:
        day += 1
        count_day -= 1
        days_month = months(month, year)
        if day > days_month:
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1

    return(day,month,year)

print(days_ad(17,12,2026,25))


FILE = Path("pat")
DATA = FILE /"pat.json"

DIR_DATA = "data/block_15/numbers"

DATA.parent.mkdir(parents=True, exist_ok=True)
with open(DATA,"w") as file:
    json.dump(repeat_numbers, file)

json_list = []
for key,values in repeat_numbers.items():
    key = str(key)
    value = str(values)
    dict = f'"{key}":{value}'

    json_list.append(dict)

new = ", ".join(json_list)

json_final = f'{{{new}}}'
print(json_final)

numbers_ramdom: list[int] = [10, 25, 37, 42, 58, 63, 71, 84, 96, 100]
actual = datetime.datetime.today()
sec_now = actual.second

module = sec_now % len(numbers_ramdom)
print(numbers_ramdom[module])



print(random.choice(numbers_ramdom))




















