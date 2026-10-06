from block_17.validate_name import validate_name

def test_validate_name():
    name: str = validate_name("Juan")
    assert name