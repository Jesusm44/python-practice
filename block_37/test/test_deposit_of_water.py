import pytest
from block_37.deposit_of_water import DepositOfWater

def test_precontition_capacity():
    tank_water = DepositOfWater(
        maximum_capacity=52,
        current_capacity=10
    )
    assert tank_water.current_capacity == 10

def test_postcondition_capacity():
    tank_water = DepositOfWater(
        maximum_capacity= 52,
        current_capacity= 42
    )
    tank_water.add_liters(10)
    assert tank_water.current_capacity == 52 

def test_failed_invariant():
    with pytest.raises(ValueError):
        tank_water = DepositOfWater(
            maximum_capacity=52,
            current_capacity=105
        )

def test_failed_invariant_Add():
    tank_water = DepositOfWater(
        maximum_capacity=52,
        current_capacity=40
    )
    with pytest.raises(ValueError):
        tank_water.add_liters(-5)
        tank_water.add_liters(0)
        tank_water.add_liters(50)

def test_failed_invariant_extrac():
    tank_water = DepositOfWater(
        maximum_capacity=52,
        current_capacity=40
    )
    with pytest.raises(ValueError):
        tank_water.extract_liters(41)

def test_save_last_capacity():
    tank_water = DepositOfWater(
            maximum_capacity=52,
            current_capacity=40
        )
    last_capacity = tank_water.current_capacity

    with pytest.raises(ValueError):
        tank_water.add_liters(52)
    
    assert tank_water.current_capacity == last_capacity