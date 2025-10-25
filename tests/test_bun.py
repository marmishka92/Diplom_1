import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self,):
        bun = Bun(name='Краторная булка N-200i', price=1255)
        bun.get_name()
        assert bun.get_name() == 'Краторная булка N-200i'

    def test_get_price(self):
        bun = Bun(name='Краторная булка N-200i', price=1500)
        bun.get_price()
        assert bun.get_price() == 1500