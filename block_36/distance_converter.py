class Kilometers:
    def __init__(self,kilometers) -> None:
        self.kilometers = kilometers

    def kilometers_to_meters(self):
        distance_in_meters = (self.kilometers * 1000)
        return distance_in_meters

    def kilometers_to_centimeters(self):
        distance_in_centimeters = (self.kilometers * 100000)
        return distance_in_centimeters

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371
    
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.609344

kilometers = Kilometers(25)
print(kilometers.kilometers_to_miles(10))
print(kilometers.miles_to_kilometers(25))
print(kilometers.kilometers_to_meters())
print(kilometers.kilometers_to_centimeters())
