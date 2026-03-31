import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE))
    return burger


class TestBurger:
    def test_set_buns(self, burger):
        assert burger.bun.get_name() == Data.BLACK_BUN

    def test_add_ingredient(self, burger):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == Data.HOT_SAUCE

    def test_remove_ingredient(self, burger):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == Data.CUTLET

    def test_get_price(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE))
        assert burger.get_price() == Data.BLACK_BUN_PRICE * 2 + Data.CUTLET_PRICE

    def test_get_receipt(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE))
        receipt = burger.get_receipt()
        assert Data.BLACK_BUN in receipt
        assert Data.HOT_SAUCE in receipt
