from more_itertools import first


def convert_int(name) -> float | ValueError:
    try:
        convert = float(name)
        return (convert)
    except ValueError as error:
        return error

def delete_student(students, name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
        else:
            print("Student", name, "not found")
    return students

users = {
    "age" : 25,
    "city": ["Caraca, Guayaquil"]
}
def search_key(users):
    key_search = input("search your key: ")
    try:
        value = users[key_search]
        print("Key found")
        print(value)
    except KeyError as error:
        print(f"Key not found: {error}")

numbers = []

def obtain_elements(numbers):
    try:
        first_element = numbers[0]
        print("element obtained", first_element)
    except IndexError as error:
        print(f'Element not found, {error}')














