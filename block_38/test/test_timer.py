import pytest
from block_38.timer import Timer


def test_save_after_time():
    timer = Timer(
        time="17:52"
    )

    before_time = timer.time

    timer.consult_time()

    after_time = timer.time

    assert after_time == before_time