from unittest import TestCase
from product import Product

class TestProduct(TestCase):
    def test_is_valid_when_no_fields_set(self):
        product = Product()
        product.name = ""
        product.description = ""
        product.unit_cost = ""
        product.barcode_number = ""
        product.stock_count = 0
        product.discount_amount = 0

        self.assertEqual(product.is_valid(), False)

    def test_is_valid_when_all_fields_set(self):
        product = Product()
        product.name = "Apple"
        product.description = "A delicious fruit"
        product.unit_cost = 1.50
        product.barcode_number = "abc123"
        product.stock_count = 5
        product.discount_amount = 0

        self.assertEqual(product.is_valid(), True)