import operations

def main():
    a = int(input("Enter any number: "))
    b = int(input("Enter another number: "))

    print(f'The addition is: {operations.addition(a,b)}')
    print(f'The subtraction is: {operations.subtraction(a,b)}')


if __name__ == "__main__":
    main()