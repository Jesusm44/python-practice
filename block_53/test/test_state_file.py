import pytest
from block_53.state_file import States

def test_file():
    state = States()
    assert state.state == False

def test_in_with():
    state = States()
    with pytest.raises(ValueError):
        with state:
            assert state.state == True
            raise ValueError("The state must shut down")
    assert state.state == False