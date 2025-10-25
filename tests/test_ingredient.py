import pytest
from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_ingredients(self):
        ingredient = Ingredient(ingredient_type= INGREDIENT_TYPE_FILLING, name="cutlet", price=200)
        assert ingredient.get_price() == 200

    def test_get_name_ingredients(self):
        ingredient = Ingredient(ingredient_type= INGREDIENT_TYPE_SAUCE, name="chili sauce", price=200)
        assert ingredient.get_name() == "chili sauce"

    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE],
                                                              [INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE],
                                                              [INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE],
                                                              [INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE],
                                                              [INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE],
                                                              [INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE]])
    def test_get_type_ingredients(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_type() == ingredient_type