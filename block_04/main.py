import users 

def main() -> None:
    name = str(input("Enter your name: ")).capitalize()
    print(users.create_user(name))

if __name__ == "__main__":
    main()