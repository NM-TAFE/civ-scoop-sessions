# CLI Runner goes here
from product import Product
from shopping_cart import ShoppingCart
from shopfront import Shopfront

shopfront = Shopfront()
shopping_cart = ShoppingCart()

def print_menu():
    print("Welcome to the shop")
    print("Press numbers to do things:")
    print("1. List all items in the shop")
    print("2. Add items to cart")
    print("3. List Items in cart") # Exercise
    print()
    print("9. To quit")


def setup_products():
    shopfront.add_product(Product("Apple", "A fruit", 150, "abc123", 100))
    shopfront.add_product(Product("Orange", "A fruit", 250, "abc321", 100))
    shopfront.add_product(Product("Velcro", "A convenient object", 500, "zxc123", 100))
    shopfront.add_product(Product("Teabags", "A delicious drink", 800, "tes123", 100))

setup_products()
while True:
    print_menu()
    user_selection = input("Which option do you want? ")
    if user_selection not in ['1', '2', '3', '9']:
        print("Pick a valid number")
        continue
    if user_selection == '1':
        print(shopfront)
    elif user_selection == '2':
        barcode = input("Enter the barcode number: ").lower().strip()
        product = shopfront.get_product_by_barcode(barcode)
        if product is not None:
            try:
                quantity = input("Please enter how many you want as a number: ")
                quantity = int(quantity)
            except ValueError:
                quantity = 1
            shopping_cart.add_product(product, quantity)
            # Exercises: catch errors and tell the user why things failed?
    elif user_selection == '3':
        print(shopping_cart)
    elif user_selection == '9':
        print("Goodbye!")
        break


