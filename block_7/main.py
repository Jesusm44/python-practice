from typing import Any
import storage

name = input("Enter your name: ")

def main() -> list[dict[Any,Any]]:
    try:
        storage.save_user(name)
    except ValueError as error:
        print(error)

    return storage.users

if __name__ == "__main__":
    print(main())