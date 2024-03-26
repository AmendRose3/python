# 58
# Implement a Python class named `Rectangle` that is initialized 
# with `length` and
# `width`. Include the following methods:
# - `calculate_area()` that returns the area of the rectangle.
# - `calculate_perimeter()` that returns the perimeter of the rectangle.
# Additionally, create a method `display()` that prints
# the length, width, area, and
# perimeter of the rectangle.
class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def calculate_area(self):
        self.area=self.l*self.w
        print(self.area)
    def calculate_perimeter(self):
        self.p=2*(self.l+self.w)
        print(self.p)
    def display(self):
        print(f"length: {self.l}")
        print(f"Width: {self.w}")
        print(f"area: {self.area}")
        print(f"Perimeter: {self.p}")
r1=rectangle(2,5)
r1.calculate_area()
r1.calculate_perimeter()
r1.display()
