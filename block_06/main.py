import users

def main():
    name = str(input("Enter your name: "))

    print (users.create_user(name=name))

if __name__ == "__main__":
    main()