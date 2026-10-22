class Battery:
    def __init__(self, level) -> None:
        if level < 0 or level > 100:
            raise ValueError("ERROR: Battery isn't not valid.")
        self.level = level

    def charge(self,quantity):
        new_quantity = self.level + quantity
        if new_quantity >= 100:
            raise ValueError("ERROR: quantity cannot be less than 0")
        self.level = new_quantity
    
    def discharge(self, quantity):
        if quantity <= 0:
            raise ValueError("ERROR: quantity cannot be less than 0")
        
        new_quantity = self.level - quantity
        if new_quantity <=0:
            raise ValueError("ERROR: quantity cannot be less than 0")
        self.level = new_quantity

    def obtain_battery(self):
        return self.level