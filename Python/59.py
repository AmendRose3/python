# # Design a class hierarchy for a vehicle management system where `Vehicle` is the 
# base **
# # class with common attributes like `make`, `model`, and `year`.** Derive two 
# subclasses
# # from it: `Car` and `Motorcycle`, each having specific attributes like `car_type` 
# (SUV,
# # Sedan, etc.) for `Car` and `has_sidecar` (True/False) for `Motorcycle`. Implement
# an
# # initialization method for each class that appropriately uses `super()` to 
# leverage the
# # base class `__init__`. Include a method `display_vehicle_info()` in each class to
# print
# # the vehicle's details.
class Vehicle:#base class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,make,model,year,car_type):
        super().__init__(make,model,year)
        self.car_type=car_type
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"car_type: {self.car_type}")
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,has_sidecar):
        super().__init__(make,model,year)
        self.has_sidecar=has_sidecar
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"has_sidecar: {self.has_sidecar}")
car1=Car('A','ABC123',2024,'SUV')
motor1=Motorcycle('B','HIJ678',2013,True)
car1.display()
motor1.display()
