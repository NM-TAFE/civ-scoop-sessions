from payment import Payment
from random import choice

class DirectEntryPayment(Payment):
    def execute(self):
        print("Connected to the whatever exchange")
        print(f"Sent ${self.amount/100} to {self.payee} from {self.payer}")
        result = choice([True, False])

        self.settled = result
        return self.settled
    
    def validate(self):
        """A payment is valid if the amount is positive"""
        if self.amount > 0:
            return True
        return False
        # return self.amount > 0