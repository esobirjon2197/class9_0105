
# 9-m
class Vehicle:
    def __init__(self, speed, weight, fuel_type):
        self.speed = speed
        self.weight = weight
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.speed} tezlikda harakatlanmoqda")


class Bike(Vehicle):
    def __init__(self, speed, weight, fuel_type, bike_type, gear):
        super().__init__(speed, weight, fuel_type)
        self.bike_type = bike_type
        self.gear = gear

    def drive(self):
        super().drive()
        print(f"Bike turi: {self.bike_type}")


b = Bike(60, 15, "yo‘q", "Sport", 6)
b.drive()
