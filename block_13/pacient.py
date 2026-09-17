import datetime

users = []

def valid_name(name):
    if not isinstance(name,str) or len(name)< 3:
        raise ValueError("Name not valid")
    if not name.strip():
        raise ValueError("Name not by empty")
    return name

def valid_age(age):
    if not isinstance(age,int) or age not in range(0,121):
        raise ValueError("Age not valid")
    return age

def create_user():
    register = datetime.date.today()

    name = input("Enter name: ").capitalize()
    age = int(input("Enter age: "))

    valid_n = valid_name(name)
    valid_e= valid_age(age)

    create_user = {
        "name": valid_n,
        "age": valid_e,
        "subscription" : register
    }

    users.append(create_user)
    return create_user

print(create_user())

def days_since(user):
    delta = datetime.date.today() - user["subscription"]
    return delta.days

def future_date(user):
    date = user["subscription"] + datetime.timedelta(days=30)
    print(f"You need to pick up your card on {date}.")