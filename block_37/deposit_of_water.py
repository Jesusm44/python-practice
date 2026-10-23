class DepositOfWater:
    def __init__(self,maximum_capacity,current_capacity) -> None:
        if not(0 <= current_capacity <= maximum_capacity):
            raise ValueError("ERROR: You are out of range.")
        
        self.maximum_capacity = maximum_capacity
        self.current_capacity = current_capacity

    def add_liters(self, liters):
        if liters <= 0:
            raise(ValueError("ERROR: cannot add 0 or negative quantities"))

        add_liters = self.current_capacity + liters
        if add_liters > self.maximum_capacity:
            raise ValueError("ERROR: maximum capacity exceeded")
        
        self.current_capacity = add_liters

    def extract_liters(self,liters):
        if liters <= 0:
            raise ValueError("ERROR: cannot extract 0 or negative quantities")

        extract_liters = self.current_capacity - liters
        if extract_liters < 0:
            raise ValueError("ERROR: You cannot run out of water")
        self.current_capacity = extract_liters

    @staticmethod
    def show_current_capacity(current_capacity):
        print(f'Your current quantity is: {current_capacity}L')


water_tank = DepositOfWater(52,10)
water_tank.show_current_capacity(water_tank.current_capacity)