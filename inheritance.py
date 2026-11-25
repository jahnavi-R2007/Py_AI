class vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        return f"{self.brand} engine started"
class car(vehicle):
    def drive(self):
        return f"{self.brand} car is driving"
my_car = car("Toyota")
print(my_car.start())
print(my_car.drive())