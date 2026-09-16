import math

numbers: list[float] = [12, 45, 7.2, 23.5, 89, 34, 56, 3, 78, 21]

for number in numbers:
    print(f'---{number}---')
    print(f'The square root of {number} is: {math.sqrt(number):.2f}')
    print(f'The rounding of the {number} is: {math.ceil(number)}')
    print(f'Rounding down the {number} is: {math.floor(number)}')
    if isinstance(number, int):
        print(f'The factorial of the {number} is: {math.factorial(number)}')

def area_circle_grades_radianes():
    PI = math.pi
    radius = float(input("Enter the radius of your circle: "))
    area = PI * math.pow(radius,2)

    DEGREES = 360
    radians = math.radians(DEGREES)

    print(f'The area of the circle is: {area:.2f}')
    print(f'Radians are {radians:.2f}')

area_circle_grades_radianes()
