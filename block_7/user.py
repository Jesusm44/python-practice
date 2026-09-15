def create_user(name):
    if not name.strip():
        raise ValueError("The name cannot be empty.")

    return name