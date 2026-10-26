import pytest
from block_42.failure_2 import User

def test_get_domain():
    user_test = User(
        name="Juan",
        email="pussydestroyer@gmail.com"
    )
    get_domain = user_test.get_domain(
        email=user_test.email
    )
    assert get_domain == "gmail.com"

def test_change_name():
    user = User(
        name="Juan",
        email="pussydestroyer@gmail.com"
    )
    user.change_name(
        new_name="Margarito"
    )
    assert user.name == "Margarito"

def test_from_email():
    user = User(
        name="Juan",
        email="pussydestroyer@gmail.com"
    )
    new_user = user.from_email(
        email=user.email
    )
    assert new_user.name == "pussydestroyer"
    assert new_user.email == "pussydestroyer@gmail.com"

def test_valid_email():
    user = User(
        name="Juan",
        email="juan_y_maria@gmail.com"
    )

    valid_email = user.is_valid_email(
        email=user.email
    )

    with pytest.raises(ValueError):
        user_2 = User(
            name="Maria",
            email="@gmail.com"
        )
        
    assert valid_email is True
    assert User.is_valid_email("@gmail.com") is False








