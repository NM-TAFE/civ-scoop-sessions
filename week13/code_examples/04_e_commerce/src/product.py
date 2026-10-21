class Product:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.unit_cost = ""
        self.barcode_number = ""
        self.stock_count = 0
        self.discount_amount = 0

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
                f"${round(self.unit_cost/100, 2)}\n" + \
                f"{self.barcode_number}"
