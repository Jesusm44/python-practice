from validation import validation_name

def create_user(name:str) -> str | None:
    new_name: None | str  = validation_name(name)

    if new_name is not None:
        return "User created"

    return None