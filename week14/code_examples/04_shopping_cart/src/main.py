from cart_item import CartItem
from product import Product
from shopping_cart import ShoppingCart

list_of_products = [
    Product("apples", 200, 600),
    Product("oranges", 300, 150)
]

shopping_cart = ShoppingCart()

def print_menu():
    print("Enter an option:")
    print("1. to print all items")
    print("2. to select an item to add to your cart")
    print("3. to view your cart")
    print("4. to check out")
    print("5 or q to quit")

while True:
    print_menu()
    raw_input = input("What option do you pick? ").lower().strip()
    if raw_input == 'q' or raw_input == '5':
        print("Thanks for shopping with us")
        break

    if raw_input == '1':
        id = 0
        for product in list_of_products:
            print(id, product)
            id += 1

    if raw_input == '2':
        last_index = len(list_of_products) - 1
        print(f"Enter the id of the item you want, from 0 to {last_index}")
        try:
            item_id = int(input("Which product do you want? "))
            if item_id < 0 or item_id > last_index:
                raise ValueError("Item ID out of range")
            quantity = int(input("How many of these do you want? "))

            cart_item = CartItem(list_of_products[item_id], quantity)
            shopping_cart.add_item(cart_item)
        except ValueError:
            print("Enter a valid number!")

    if raw_input == '3':
        print(shopping_cart)