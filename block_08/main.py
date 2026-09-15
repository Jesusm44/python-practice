import users
import storage

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    active = True

    try:
        user = users.create_user(name, age, active)
        storage.save_user(user)
        print("User created successfully.")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()