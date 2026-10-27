class Record:
    def __init__(self, event_one, event_two) -> None:
        self.event_one = event_one
        self.event_two = event_two
        self.events = []

    def add_events(self):
        self.events.append(self.event_one)
        self.events.append(self.event_two)


a = Record("Enter", "Exit")
final_a = a.add_events()
b = Record("Exit", "Enter")

print(a is not b)
print(a.events is not b.events)

x = ["apple, watermelon"]

a  = {
    "fruits" : x
}

b = {
    "fruits" : x
}

print(a["fruits"] is b["fruits"])

a["fruits"].append("banana")

print("banana" not in b["fruits"])
print(id(a))
print(id(b))

x = ["watermelon", "banana"]

a  = {
    "fruits" : x
}

print(a["fruits"] == b["fruits"])
print(a)
print(b)
