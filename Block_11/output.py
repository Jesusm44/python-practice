from typing import LiteralString
from student import students
import validation

def show_menu() -> LiteralString:
    return f"""
    --- Options ---
    1. Register user
    2. Search student
    3. Delete student
    4. Show students
    5. Exit"""

def show_menu_students():
    return f"""
    ---Options---
    1. Show student
    2. Show students
    3. Exit"""

def show_student(students,name)-> bool:
    valid_name = validation.validation_name(name).capitalize() 

    for student in students:
        if student["name"] == valid_name:
            print(f"""
            Name: {student["name"]}
            Age: {student["age"]}
        """)
            return True

    return False

def show_students(students) -> None:
    for student in students:
        print(f"""
        Name: {student["name"]}
        Age: {student["age"]}""")

def show_messages(message) -> None:
    print(message)

def show_error(error) -> None:
    print(error)


