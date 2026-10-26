class Tank:
    def __init__(self, capacity, current_amount):
        if capacity <= 0:
            raise ValueError("Invalid capacity")
        
        if not(0<= current_amount <= capacity):
            raise ValueError("Invalid initial amount")
        
        self.capacity = capacity
        self.current_amount = current_amount

    def add(self, liters):
        if liters <= 0:
            raise ValueError("Liters must be positive")

        new_capacity = self.current_amount + liters

        if new_capacity > self.capacity:
            raise ValueError("Maximum capacity exceeded")
        self.current_amount = new_capacity

    def extract(self, liters):
        if liters <= 0:
            raise ValueError("Liters must be positive")
        extract_capacity = self.current_amount - liters

        if extract_capacity < 0:
            raise ValueError("Not enough water")
        self.current_amount = extract_capacity
