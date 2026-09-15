from typing import Any
from user import create_user

users:list[dict] = []

def save_user(name) -> list[dict[Any, Any]]:
    new_name: Any = create_user(name)

    user_dict: dict[str,Any] = {
        "name": new_name,
        "active": True
    }

    users.append(user_dict)

    return users