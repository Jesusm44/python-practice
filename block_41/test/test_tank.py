import pytest
from block_41.failure import Tank

def test_fail_extract():
    tank = Tank(
        capacity=100,
        current_amount=100
    )
    with pytest.raises(ValueError):
        tank.extract(101)