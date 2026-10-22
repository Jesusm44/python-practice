import pytest
from block_31.battery import Battery

def test_show_battery():
    battery = Battery(80)
    assert battery.level == 80

def test_invali_show_battery():
    with pytest.raises(ValueError):
        Battery(-10)

def test_battery_zero():
    battery = Battery(0)
    assert battery.level == 0

def test_battery_one_houndred():
    battery = Battery(100)
    assert battery.level == 100

def test_valid_charge():
    battery = Battery(40)
    charge = battery.charge(50)

    assert battery.level == 90

def test_invalid_charge_battery():
    battery = Battery(90)
    with pytest.raises(ValueError):
        charge = battery.charge(90)

def test_valid_consumption():
    battery = Battery(50)
    discharge = battery.discharge(40)

    assert battery.level == 10

def test_consumption_less_than_zero():
    battery = Battery(40)
    with pytest.raises(ValueError):
        discharge = battery.discharge(50)

def test_quantity_zero():
    battery = Battery(40)
    with pytest.raises(ValueError):
        discharge = battery.discharge(0)

def test_negative_battery():
    with pytest.raises( ValueError):
        battery = Battery(-25)

def test_invalid_charge_keeps_previous_level():
    battery = Battery(90)
    with pytest.raises(ValueError):
        battery.charge(20)
    assert battery.level == 90

def test_invalid_discharge_keeps_previous_level():
    battery = Battery(10)
    with pytest.raises(ValueError):
        battery.discharge(20)
    assert battery.level == 10












