from unittest import TestCase

from shopping_cart import ShoppingCart
from cart_item import CartItem
from product import Product

class TestShoppingCart(TestCase):
    def test_add_product_valid_cart_item_works(self):
        shopping_cart = ShoppingCart()
        product = Product(stock_count=1)

        shopping_cart.add_product(product, 1)
        self.assertEqual(len(shopping_cart.products), 1)

    def test_add_product_not_valid_cart_item_fails(self):
        shopping_cart = ShoppingCart()
        product = Product(stock_count=1)

        shopping_cart.add_product(product, 2)
        self.assertListEqual(shopping_cart.products, [])