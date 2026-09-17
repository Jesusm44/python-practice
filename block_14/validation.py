def validation_name(name):
    if not isinstance(name, str) or len(name) < 3:
        raise ValueError("The name is incorrect.")
    if not name.strip():
        raise ValueError("The name cannot be empty; it must have at least 3 characters.")
    return name

def validation_age(age):
    if not isinstance(age,int):
        raise ValueError("The age is incorrect.")
    if age not in range(1,121):
        raise ValueError("The age is out of range; the age must be between 1 and 120 years.")
    return age

