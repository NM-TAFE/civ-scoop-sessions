# E-Commerce

Let's build an e-commerce platform for the CLI.


- Product
    - Name
    - Description
    - Unit Cost
    - BarcodeNumber
    - StockCount
    - DiscountAmount (default: 0)
    * is_valid()

- Shopfront
    - products

- ShoppingCart
    - Products -> unit number
    - user_email
    * add_product(product, quantity)

- CartProductItem


---

## Design thoughts

{
    "barcode": 123
}

CartItem
- product
- quantity

given add_product is_called
when the cart_item is valid
then shopping_cart instance's products list should in length by 1


given that we create a cart item
when the quantity specified is lte the stock count of the product
then it is valid
