import pytest
from block_41.failure import Deposito

def test_fail_extract():
    tank = Deposito(
        capacidad=100,
        cantidad_actual=100
    )
    with pytest.raises(ValueError):
        tank.extraer(101)