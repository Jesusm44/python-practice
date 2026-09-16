import calculator

def show_operation():
    operation = True

    while operation:
        a = float(input("Enter any number: "))
        b = float(input("Enter any number: "))

        options = int(input(f"""
options:
1. addition
2. subtract
3. multiply
4. division
5. exit
chosise option: """))

        if options == 1:
            print(calculator.addition(a,b))
        elif options == 2:
            print(calculator.subtract(a,b))
        elif options == 3:
            print(calculator.multiply(a,b))
        elif options == 4:
            try:
                print(calculator.division(a,b))
            except ZeroDivisionError as error:
                print(error)
        elif options == 5:
            print("Exit calculator...")
            operation = False
        else:
            print("ERROR: This option does not exist.")


def main():
    show_operation()

if __name__ == "__main__":
    main()


        
