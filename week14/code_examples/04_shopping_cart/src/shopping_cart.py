from cart_item import CartItem

class ShoppingCart:
    def __init__(self, items=None):
        self.__items = items or []

    def add_item(self, item):
        if not isinstance(item, CartItem):
            return  # Guard clause
        
        if item.is_valid():
            self.__items.append(item)
        else:
            print("This item didn't have enough stock")

    def __str__(self):
        string = ""
        for item in self.__items:
            string += str(item.product) + "\n"  # Gross! Breaks encapsulation
        return string

    def checkout(self):
        # go through products and deduct the stock amount
        # print total cart price for payment
        pass