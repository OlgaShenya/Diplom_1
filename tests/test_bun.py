import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [
        ('White bun', 100.0),
        ('black bun', 200.0),
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        ('White bun', 100.0),
        ('black bun', 200.0),
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
