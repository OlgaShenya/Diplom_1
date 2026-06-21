import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def database():
    return Database()


class TestDatabase:

    def test_available_buns_count(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_count(self, database):
        assert len(database.available_ingredients()) == 6

    @pytest.mark.parametrize('index, expected_name, expected_price', [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300),
    ])
    def test_available_buns_content(self, database, index, expected_name, expected_price):
        buns = database.available_buns()
        assert isinstance(buns[index], Bun) and buns[index].get_name() == expected_name and buns[index].get_price() == expected_price

    @pytest.mark.parametrize('index, expected_type, expected_name, expected_price', [
        (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (5, INGREDIENT_TYPE_FILLING, 'sausage', 300),
    ])
    def test_available_ingredients_content(
            self, database, index, expected_type, expected_name, expected_price
    ):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients[index], Ingredient) and ingredients[index].get_type() == expected_type and ingredients[index].get_name() == expected_name and ingredients[index].get_price() == expected_price
