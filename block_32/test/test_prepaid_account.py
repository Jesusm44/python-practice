import pytest
from block_32.prepaid_account import PrepeaidAccount


def test_initial_balance():
    account = PrepeaidAccount("user_a", 1000)
    with pytest.raises(ValueError):
        account.use_up_cents(1500)
    assert account.balance_cents == 1000