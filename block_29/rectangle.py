class Rectangle:
    def __init__(self,h:float,b:float) -> None:
        if h < 0:
            raise ValueError("The height cannot be less than 0")
        if b < 0:
            raise ValueError("The base cannot be less than 0")

        self.h: float = h
        self.b: float = b

    def area_rectangle(self):
        return self.h * self.b

    def perimeter_rectangle(self):
        return 2 * (self.h + self.b)


rectangle = Rectangle(10,20)

area_of_rectangle = rectangle.area_rectangle()
perimeter_of_rectangle = rectangle.perimeter_rectangle()

print(f'Area is: {area_of_rectangle}')
print(f'Perimeter is: {perimeter_of_rectangle}')

rectangle_1 = Rectangle(0,-2)
