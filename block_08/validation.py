from typing import Literal
from typing import Any


def validation_name(name) -> Any:
    if not name.strip():
        raise ValueError("The name cannot be empty.")
    return name

def validation_age(age) -> Any | Literal[False]:
    if not isinstance(age, int):
        raise ValueError("Age cannot be either a word or a decimal.")

    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    return age

def validation_active(active) -> bool:
    if not isinstance(active, bool):
        raise ValueError("Active must be a boolean.")
    return active