class Reservation:
    def __init__(self,identifier,customer,number_of_people) -> None:
        if len(identifier) < 4 and not identifier.startswith("A"):
            raise ValueError("The identification does not meet the reservation parameters.")

        if number_of_people < 0:
            raise ValueError("The reservation cannot be for fewer than 1 person.")

        if not(isinstance(customer,str) and customer.strip() and len(customer.strip())):
            raise ValueError("The client name is not valid.")

        self. identifier = identifier
        self.customer = customer.capitalize()
        self.number_of_people = number_of_people

    def __str__(self):
        return f"Welcome {self.customer} --- your table code {self.identifier}"

    def __repr__(self) -> str:
        return f"Reservation(indentifier={self.identifier!r}, customer={self.customer!r}, number_of_people={self.number_of_people!r})"

mesa_number_A = Reservation("A123", "MARIA", 12
)

print(str(mesa_number_A))
print(repr(mesa_number_A))