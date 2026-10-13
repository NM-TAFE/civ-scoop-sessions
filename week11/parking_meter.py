"""
Parking Meter class

Attributes:
- latitude
- longitude
- cost_per_hour
- minimum_parking_time

Behaviours:
quote_ticket()
print_ticket()
"""

class ParkingMeter:
    def __init__(self, latitude, longitude, cost_per_hour, minimum_parking_time):
        self.__latitude = latitude
        self.__longitude = longitude
        self.__cost_per_hour = cost_per_hour
        self.__minimum_parking_time = minimum_parking_time

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def cost_per_hour(self):
        return self.__cost_per_hour

    @property
    def minimum_parking_time(self):
        return self.__minimum_parking_time

    def quote_ticket(self, hours_requested):
        if hours_requested < self.minimum_parking_time:
            raise ValueError(f"You must park for at least {self.minimum_parking_time} hours.")

        return f"${self.cost_per_hour * hours_requested}"

    def print_ticket(self, hours_requested):
        # print(ParkingMeter.quote_ticket(self, hours_requested)) # Absolutely no reason to do this
        print(self.quote_ticket(hours_requested))