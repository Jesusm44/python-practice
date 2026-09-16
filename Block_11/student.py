from typing import Any
from entrada import read_age, read_name
import validation

students:list[Any] = []

def create_student() -> dict[str, Any]:
    name: str=   read_name().capitalize()
    age: int = read_age()
    
    valid_name: str = validation.validation_name(name)
    valid_age: int = validation.validation_age(age)

    new_student:dict[str,Any] ={
        "name" : valid_name,
        "age" : valid_age
    }
    return new_student

def save_student(students,student:dict[str,Any]) -> Any:
    students.append(student)
    return students

def search_student(students,name)  -> list[dict[str, Any]]:
    valid_name = validation.validation_name(name).capitalize()

    result:list[Any] = list(filter(lambda student: student["name"] == valid_name, students)) 
    return result
    
def delete_student(students,name) -> bool:
    valid_name = validation.validation_name(name).capitalize()
    result:list[Any] = list(filter( lambda student: student["name"] == valid_name, students))

    if result:
        students.remove(result[0])
        return True
    return False
