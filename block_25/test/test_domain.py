from block_25.domain import validate_product, create_product

def test_validate_product():
    result = validate_product(
        name="mouse",
        stock=5,
        price=25
    )
    assert result == ("mouse",5,25)

def test_create_product():
    product = create_product(
        name = "mouse",
        stock = 5,
        price = 25
    )

    assert product == {
        "name" : "mouse",
        "stock": 5,
        "price": 25
    }