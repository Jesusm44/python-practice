class Products:
    def __init__(self,code,name,stock) -> None:
        if not code.startswith("A"):
            raise ValueError("ERROR: The code is not valid.")
        if len(code) != 4:
            raise ValueError("ERROR: The code is not valid")

        if not (isinstance(name,str) and name.strip() and not len(name.strip()) < 3):
            raise ValueError("ERROR: Invalid name")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self.code = code
        self.name = name
        self.stock = stock

    def consult_stock(self):
        return self.stock

    def add_stock(self, add_stock):
        if add_stock <= 0:
            raise ValueError("The stock entered cannot be less than or equal to 0")
        new_stock = add_stock + self.stock
        self.stock = new_stock

    def reduce_stock(self, substrack_stock):
        if substrack_stock <= 0:
            raise ValueError("The stock to be subtracted cannot be less than or equal to 0.")
        new_stock = self.stock - substrack_stock
        if new_stock < 0:
            raise ValueError("You cannot subtract stock that isn't there.")
        self.stock = new_stock

    @classmethod
    def from_text(cls, text):
        parts = text.split(",", 2)

        data = {
            "code": parts[0],
            "name": parts[1],
            "stock": int(parts[2])
        }

        return cls(**data)