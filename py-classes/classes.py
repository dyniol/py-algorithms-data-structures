class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    # def seating_capacity(self, capacity):
    #     return f"The seating capacity of a {self.name} is {capacity} passangers"

class Bus(Vehicle):
    pass
    # def seating_capacity(self, capacity=50):
    #     return super().seating_capacity(capacity=50)
class Car(Vehicle):
    pass

school_bus = Bus("School volvo", 240, 18)
print(
#     "Name :", school_bus.name,
#  "Speed :", school_bus.max_speed,
#  "Mileage :", school_bus.mileage,
#  "Seating Capacity :", school_bus.seating_capacity()
    school_bus.color)