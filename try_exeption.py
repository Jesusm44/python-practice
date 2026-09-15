number_one: str = input("Enter any number: ")
number_two: str = input("Enter any number: ")

def create_division(a,b) -> None:
    try:
        a = int(a)
        b = int(b)
        result:float | int = a / b
    except ValueError:
        print("One of the two variables is a letter, not a number.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(result)
    finally:
        print("Operation complete")

create_division(
        a= number_one, 
        b= number_two
    )