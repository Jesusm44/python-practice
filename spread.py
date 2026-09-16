def convert_number():
    print("---Convert str(number) a int(number)---")
    number = input("Enter any number: ")
    convert_number = int(number)
    return convert_number


def process_number():
    VAT = 0.12 
    number = convert_number()
    result = number * (1 + VAT)
    return result

def main():
    try:
        print(f'The VAT on this value is: {process_number()}')
    except ValueError as error:
        print(error)
    else:
        print("It has been processed successfully.")
    finally:
        print("Thanks, heading out now.")

if __name__=="__main__":
    main()


