from unittest import TestCase

from product import Product
from cart_item import CartItem

class TestCartItem(TestCase):
    def test_is_valid_for_too_much_quantity_false(self):
        product = Product()
        product.stock_count = 0
        cart_item = CartItem(product, 1)
        self.assertEqual(cart_item.is_valid(), False)

    def test_is_valid_for_correct_quantity_true(self):
        product = Product()
        product.stock_count = 1
        cart_item = CartItem(product, 1)
        self.assertEqual(cart_item.is_valid(), True)