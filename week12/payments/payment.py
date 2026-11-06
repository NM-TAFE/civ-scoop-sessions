from abc import ABC, abstractmethod
# ABC = Abstract Base Class

class Payment(ABC):
    def __init__(self, payee, payer, amount):
        self.payee = payee
        self.payer = payer
        self.amount = amount
        self.settled = False

    @abstractmethod
    def execute(self) -> bool:
        """ Returns true if the transaction settled """
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> bool:
        raise NotImplementedError