from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.bun import Bun


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun=bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient=ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient=ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient=ingredient_1)
        burger.add_ingredient(ingredient=ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] ==  ingredient_1
        assert burger.ingredients[0] == ingredient_2

    def test_get_price(self):
        burger = Burger()
        ingredient = Mock()
        bun = Mock()
        bun.get_price.return_value = 1997
        ingredient.get_price.return_value = 76
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)
        assert burger.get_price() == 4070

    def test_get_receipt(self):
        burger = Burger()
        ingredient = Mock()
        bun = Mock()
        bun.get_name.return_value = 'Булочка с маком'
        bun.get_price.return_value = 199
        ingredient.get_name.return_value = 'Варенье'
        ingredient.get_type.return_value = 'Динозавр'
        ingredient.get_price.return_value = 10
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)
        assert burger.get_receipt() == ('(==== Булочка с маком ====)\n'
 '= динозавр Варенье =\n'
 '(==== Булочка с маком ====)\n'
 '\n'
 'Price: 408')