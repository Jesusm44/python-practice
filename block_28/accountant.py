class Accountant:
    def __init__(self,value) -> None:
        if value < 0:
            raise ValueError("The value cannot be less than 0")
        self.value = value

    def increase(self,increment):
        self.value += increment
        return self.value
    
    def decrement(self,subtract):
        self.value -= subtract
        return self.value

    def obtain_value(self):
        print(f'The value is: {self.value}')


accountant_a = Accountant(1)
increment_accountant = accountant_a.increase(1)
show_accountant = accountant_a.obtain_value()

accountant_b = Accountant(10)
show_accountant = accountant_b.obtain_value()

