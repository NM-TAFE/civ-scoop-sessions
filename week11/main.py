from parking_meter import ParkingMeter

freo = ParkingMeter(115, 135, 20, .5)

raw_input = ""
while type(raw_input) != int:
    try:
        raw_input = input("How long do you want to park for? ")
        raw_input = int(raw_input)
    except ValueError:
        print("Please enter a number.")

freo.print_ticket(raw_input)


"""
Think about the attributes and behaviours of:
- Room
- Elevator & ElevatorQueue
- Book
- Computer
"""