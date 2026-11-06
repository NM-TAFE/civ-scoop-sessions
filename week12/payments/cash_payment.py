from payment import Payment

class CashPayment(Payment):
    def execute(self):
        if not self.validate():
            return False

        print(f"Dear {self.payer}. Please visit {self.payee}'s " +
              f"house and surprise them with ${self.amount/100}.")

        self.settled = True
        return True

    def validate(self):
        """A payment is valid if the amount is positive"""
        if self.amount > 0:
            return True
        return False
        # return self.amount > 0