 # This function allows the user to enter the name.
from traceback import print_tb


def read_name() -> str:
        name:str = input("Enter your name: ")
        return name

# The function helps us validate the names by:
    # 1. Checking that the name is a string
    # 2. Checkihat the name is not empty
def _validation_name() -> str:
    name: str = read_name()

    if not isinstance(name, str):
        raise ValueError("The name is not a string.")

    if not name.strip():
        raise ValueError("The name cannot be empty.")

    return name

# Function used to output the already validated name.
def input_name() -> str:
    name: str = _validation_name()
    return name

# The main function serves to coordinate the entire system.
def main() -> None:
    try:
        name: str = input_name()
        print(f'Your name is: {name}')
    except ValueError as error:
        print(error)

# This helps us verify that we are on the `main` branch and allows us to run all the functions.
if __name__ == "__main__":
    main()