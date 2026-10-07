from block_26.inventory import domain
import pytest

test_inventory = {
    "101a": {
        "name": "mouse",
        "price": 25,
        "stock": 5
    }
}


def test_validate_product():
    result = domain.valid_product(
        name="mouse",
        stock=5,
        price=25
    )

def test_code():
    result = domain.valid_code(
        test_inventory,
        code = "101b"
    )
    assert result == "101b"


def test_create_product():
    product = domain.create_product(
        name = "mouse",
        stock = 5,
        price = 25
    )

    assert product == {
        "name" : "mouse",
        "stock": 5,
        "price": 25
    }