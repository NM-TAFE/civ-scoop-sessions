from product import Product

class CartItem:
    def __init__(self, product, quantity):
        if not isinstance(product, Product): # Guard
            raise TypeError("Product must be of type Product.")

        self.product = product
        self.quantity = quantity

    def is_valid(self):
        return self.product.stock_count >= self.quantity

    def __str__(self):
        return f"{self.product.name}: {self.quantity}"