class ScoreCounter:
    def __init__(self, points) -> None:
        if not (isinstance(points, int) and points >= 0):
            raise ValueError("ERROR: Invalid points")
        
        self.points: int = points
        self.points_spent = 0

    def add_points(self,sum_points):
        if sum_points <= 0:
            raise ValueError("ERROR: Numbers less than or equal to 0 cannot be added.")
        self.points += sum_points 

    def extract_points(self, extract_point):
        if extract_point <= 0:
            raise ValueError("It cannot be subtracted")

        if extract_point > self.points:
            raise ValueError("You cannot subtract a value greater than the points you have.")

        new_points = self.points - extract_point
        count_extarct  = extract_point + self.points_spent

        self.points = new_points
        self.points_spent = count_extarct

    @staticmethod
    def show_point(points):
        print(f'your points are: {points}')
    
    @staticmethod
    def show_points_spent(points):
        print(f'your spent points are: {points.points_spent}')

    @classmethod
    def from_str(cls,text):
        if not isinstance(text, int):
            convert_text = int(text)
            return cls(convert_text)
        else:
            raise TypeError("Sorry, it cannot be converted.")

    @classmethod
    def convert_negative_tramp(cls, negative_points):
        if not isinstance(negative_points, int):
            raise ValueError("It can't be done")
        if negative_points > 0:
            raise ValueError("You don't need to convert the points")
        convert_to_positive = negative_points * (-1)

        return cls(convert_to_positive)