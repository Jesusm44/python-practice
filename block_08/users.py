from typing import Any, Literal
from validation import validation_name, validation_age, validation_active

def create_user(name, age, active):
    create_name: Any = validation_name(name)
    create_age: Any | Literal[False] = validation_age(age)
    create_active: bool = validation_active(active)

    return {
        "name" : create_name,
        "age" : create_age,
        "active" : create_active
    }