class Product:
    def __init__(self, 
                 name="", 
                 price_in_cents=0, 
                 stock_level=0
                ):
        self.name = name
        self.price_in_cents = price_in_cents
        self.stock_level = stock_level

    def __str__(self):
        return f"{self.name}, ${self.price_in_cents/100}, {self.stock_level} in stock"