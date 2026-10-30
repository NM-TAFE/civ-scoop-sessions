class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def is_valid(self):
        return self.quantity <= self.product.stock_level
