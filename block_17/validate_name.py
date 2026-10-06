def validate_name(name):
    if not isinstance(name, str):
        raise ValueError
    if not name.strip():
        raise ValueError
    return name

