from cart_item import CartItem

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        cart_item = CartItem(product, quantity)

        if not cart_item.is_valid(): # guard
            return

        self.products.append(cart_item)

    def __str__(self):
        final_string = ""
        for element in self.products:
            final_string += str(element) + "\n"

        return final_string