from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = 'cutlet'
    ingredient.get_type.return_value = 'FILLING'
    ingredient.get_price.return_value = 50.0
    return ingredient


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient3 and burger.ingredients[2] == ingredient1

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 300.0

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert '(==== black bun ====)' in receipt and '= filling cutlet =' in receipt and 'Price: 250.0' in receipt
