from block_26.inventory import services


def test_register_product():
    inventory = {}

    product = {
        "name": "mouse",
        "price": 25,
        "stock": 5
    }

    services.register_product(
        inventory,
        code="101a",
        product=product
    )

    assert inventory == {
        "101a": {
            "name": "mouse",
            "price": 25,
            "stock": 5
        }
    }


def test_search_product():
    inventory = {
        "101a": {
            "name": "mouse",
            "price": 25,
            "stock": 5
        }
    }

    result = services.search_product(
        inventory,
        code="101a"
    )

    assert result == {
        "name": "mouse",
        "price": 25,
        "stock": 5
    }