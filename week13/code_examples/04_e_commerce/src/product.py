class Product:
    def __init__(self, name="", description="", unit_cost=0, barcode_number="", stock_count=0, discount_amount=0):
        self.name = name
        self.description = description
        self.unit_cost = unit_cost
        self.barcode_number = barcode_number
        self.stock_count = stock_count
        self.discount_amount = discount_amount

    def is_valid(self):
        valid = len(self.name) > 1 and \
            len(self.barcode_number) > 1 and \
            len(self.description) > 1 and \
            self.unit_cost > 0

        return valid

    def __eq__(self, other):
        return self.barcode_number == other.barcode_number

    def __str__(self):
        return  f"{self.name}: {self.description}\n" + \
                f"${round(self.unit_cost/100, 2):.2f}\n" + \
                f"{self.barcode_number}"
