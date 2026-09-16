import random

users: list[str] = ["Ana","Luis","Carlos","Maria","Pedro"]

print(random.choice(users))
random.shuffle(users)
print(users)
print((random.randint(-1,9)))
print()