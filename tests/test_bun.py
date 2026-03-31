import pytest
from praktikum.bun import Bun
from data import Data


@pytest.fixture
def bun():
    return Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)


class TestBun:
    def test_get_name(self, bun):
        assert bun.get_name() == Data.BLACK_BUN

    def test_get_price(self, bun):
        assert bun.get_price() == Data.BLACK_BUN_PRICE
