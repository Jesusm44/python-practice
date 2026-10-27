class Coordinate:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, value: object) :
        if not isinstance(value,Coordinate):
            return NotImplemented

        return (self.x == value.x and self.y == value.y)

coordinate_a = Coordinate(12,10)
coordinate_b = Coordinate(12,10)

print(coordinate_a == coordinate_b)

class SameInstance:
    def __init__(self,date_a,date_b) -> None:
        final_date = []
        self.date_a = date_a
        self.date_b = date_b

        final_date.append(date_a)
        final_date.append(date_b)
        
test_same = SameInstance(12,14)

a = test_same

print(a is test_same)

a = [13,15,17]
b = a
a = [7,8,9]

print(a is b )