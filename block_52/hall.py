class Hall:
    def __init__(self,name) -> None:
        self.name = name
        self.users = []

room_one = Hall("Jose")
room_one.users.append("Maria")
room_one.users.append("Juan")
room_one.users.append("Jose")
room_one.users.append("Mara")


room_two = Hall("Lion")
room_two.users.append("Maria")
room_two.users.append("Juan")
room_two.users.append("Jose")
room_two.users.append("Mara")

print(room_one.users)
print(room_two.users)

print(room_one.users is room_two.users)