import pytest
from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
        ]
    )
    def test_get_price_name_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type
