import pytest

from block_57.new_user_session import NewUser

def test_new_user_one():
    user = NewUser(
        user="Tataduty",
        password=52789,
        ip="100.10.95",
        session_id="S001"
    )
    assert user.state_session == False
    assert user.create_session == False

    with user:
        assert user.state_session == True
        assert user.create_session == True

    assert user.state_session == False
    assert user.create_session == True

def test_new_user():
    user = NewUser(
        user="Tataduty",
        password=52789,
        ip="100.10.95",
        session_id="S001"
    )
    assert user.state_session == False
    assert user.create_session == False
    with pytest.raises(RuntimeError):
        with user:
            assert user.state_session == True
            assert user.create_session == True
            raise RuntimeError
    assert user.state_session == False
    assert user.create_session == True
        
        