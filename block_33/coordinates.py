class Coordinates:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod 
    def from_text(cls, text):
        parts = text.split(",")
        x = int(parts[0])
        y = int(parts[1])
        return cls(x,y)

firts_coordinates = Coordinates(15,17)
firts_coordinates_one = firts_coordinates.from_text("15,27")

