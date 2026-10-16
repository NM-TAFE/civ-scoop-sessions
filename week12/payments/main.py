from cash_payment import CashPayment
from direct_entry_payment import DirectEntryPayment
from payment import Payment

pay = CashPayment("Jordan", "Para", 16)
pay2 = DirectEntryPayment("Jazza", "Jordan", 16)
pay3 = "I Owe YOU"

for payment in [pay,pay2,pay3]:
    if issubclass(type(payment), Payment):
        payment.execute()
    else:
        print("What is this doing in here?")