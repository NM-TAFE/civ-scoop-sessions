from unittest import TestCase
from shopfront import Shopfront
from product import Product

class TestShopfront(TestCase):
    def test_products_are_a_list(self):
        shopfront = Shopfront()
        self.assertListEqual(shopfront.products, [])

    def test_products_must_be_products(self):
        shopfront = Shopfront()

        with self.assertRaises(TypeError):
            shopfront.add_product("")

        product = Product()

        shopfront.add_product(product)
        self.assertListEqual(shopfront.products, [product])

    def test_str_calls_products(self):
        shopfront = Shopfront()
        product = Product()
        product.name = "Apple"
        product.description = "A fruit"
        product.unit_cost = 150
        product.barcode_number = "abc123"
        shopfront.add_product(product)

        # Bad test?
        # Okay for now though!
        self.assertEqual(str(shopfront), "Apple: A fruit\n$1.5\nabc123\n")
        # To fix this, we want to mock and stub!