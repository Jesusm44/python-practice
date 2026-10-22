class PrepeaidAccount:
    def __init__(self, holder, balance_cents) -> None:
        self.holder = holder
        self.balance_cents = balance_cents

    def recharge(self,quantity_cents):
        if quantity_cents <= 0:
            raise ValueError("ERROR: The quantity cannot be less than 0.")

        new_balance_cents = self.balance_cents + quantity_cents
        if new_balance_cents < 0:
            raise ValueError("ERROR: The balance cannot be less than 0")
        self.balance_cents = new_balance_cents

    def use_up_cents(self,quantity_cents):
        if quantity_cents <= 0:
            raise ValueError("ERROR: The quantity cannot be less than 0.")
        new_balance_cents = self.balance_cents - quantity_cents
        if new_balance_cents < 0:
            raise ValueError("ERROR: The balance cannot be less than 0")
        self.balance_cents = new_balance_cents

    def obtain_search(self):
        return self.balance_cents


cuenta_a = PrepeaidAccount("Ana", 120)
cuenta_b = PrepeaidAccount("Pedro", 2500)
recharge = cuenta_a.recharge(120)
use_up = cuenta_a.use_up_cents(10)
recharge_two = cuenta_a.recharge(52) 
print(cuenta_a.obtain_search())
print(cuenta_b.obtain_search())