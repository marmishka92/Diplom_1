import pytest
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data


@pytest.fixture
def database():
    return Database()


class TestDatabase:
    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)

    def test_get_ingredient_by_type(self, database):
        sauces = database.find_ingredient_by_type(INGREDIENT_TYPE_SAUCE)
        fillings = database.find_ingredient_by_type(INGREDIENT_TYPE_FILLING)
        assert all(i.get_type() == INGREDIENT_TYPE_SAUCE for i in sauces)
        assert all(i.get_type() == INGREDIENT_TYPE_FILLING for i in fillings)
