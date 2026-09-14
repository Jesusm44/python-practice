def validation_name(name:str) -> None | str:
    if not isinstance(name,str):
        return None

    if name.strip() == "":
        return None

    return name