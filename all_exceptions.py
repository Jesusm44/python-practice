def main():
    def value_error():  
        try:
            age = input("Enter your age: ")
            convert_age = int(age)
            print(f'Your age is: {convert_age}')
        except ValueError as error:
            print(error)

    def type_error():
        try:
            print("Addition str + int.")
            a = input("enter any wor: ")
            b= int(input("enter any number: "))
            result = a+ b
            print(result)
        except TypeError as error:
            print(error)

    def key_error():
        users = {
            "name" : "juan",
            "age": 25
        }
        key_search = input("search your key: ")
        try:    
            value = users[key_search]
            print(value)
        except KeyError as error:
            print("Key not found:", error)

    def index_error():
        user_numbers =[]
        try:
            first_user = user_numbers[0]
            print(first_user)
        except IndexError as error:
            print(error)

    def file_not_found():
        try:
            file = open("arch_inexisten.txt", "r")
            content = file.read()
            print(content)
            file.close
        except FileNotFoundError as error:
            print(error)

    def zero_error():
        a = float(input("Enter any number: "))
        b = float(input("Enter any number: "))
        try:
            result = a / b
            print(result)
        except ZeroDivisionError as error:
            print(error)

    value_error()
    type_error()
    key_error()
    index_error()
    file_not_found()
    zero_error()

if __name__ == "__main__":
    main()












