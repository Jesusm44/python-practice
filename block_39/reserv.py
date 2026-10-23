class Reservation:
    def __init__(self, code, customer, seats, total_price):
        if seats <= 0:
            raise ValueError("Seats must be positive")

        if total_price < 0:
            raise ValueError("Price cannot be negative")

        if not customer.strip():
            raise ValueError("Customer cannot be empty")

        customer = customer.strip()
        if len(customer) < 3:
            raise ValueError("ERROR: The client's name cannot be less than 3 characters long.")
        
        self.code = code
        self.customer = customer
        self.seats = seats
        self.total_price = total_price
        self.confirmed = False

    def get_customer(self):
        return self.customer

    def is_confirmed(self):
        return self.confirmed

    def confirm(self):
        if self.confirmed == False:
            self.confirmed = True
        else:
            raise ValueError("ERROR: The confirmation has already been made")

    def change_seats(self, seats):
        if not isinstance(seats, int):
            raise ValueError("ERROR: Seats must be an integer.")

        if seats <= 0:
            raise ValueError("ERROR: Seats must be greater than 0.")

        self.seats = seats

    def apply_discount(self,discount):
        if discount <= 0:
            raise ValueError("ERROR: The discount cannot be 0 or a smaller number.")
        
        discount_amount = (self.total_price * discount) / 100
        new_price = self.total_price - discount_amount

        if new_price < 0:
            raise ValueError("ERROR: Sorry, the discount cannot be a number less than 0.")
        
        self.total_price = new_price
