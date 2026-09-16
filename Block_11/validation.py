def validation_name(name:str) -> str:
    if not isinstance(name,str):
        raise ValueError("The name must be a single word.")

    if len(name) < 3:
        raise ValueError("The name cannot be less than 3 characters long.")

    if not name.strip():
        raise ValueError("The name cannot be empty.")

    return name


def validation_age(age:int) -> int:
    if not isinstance(age, int):
        raise TypeError("The age must be a whole number, not a word.")

    if age not in range(0,121):
        raise ValueError("Age outside the 0 to 120 range")

    return age