from product import Product

class Shopfront:
    def __init__(self):
        self.products = []

    def add_product(self, new_product):
        if not isinstance(new_product, Product): # Guard clause!
            raise TypeError("Must be a Product object")

        self.products.append(new_product)

    def __str__(self):
        # Good
        all_products = ""
        for product in self.products:
            all_products += (str(product)) + "\n"
        return all_products
