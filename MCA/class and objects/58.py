# 58
# Implement a Python class named `Rectangle` that is initialized 
# with `length` and
# `width`. Include the following methods:
# - `calculate_area()` that returns the area of the rectangle.
# - `calculate_perimeter()` that returns the perimeter of the rectangle.
# Additionally, create a method `display()` that prints
# the length, width, area, and
# perimeter of the rectangle.
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.area = 0  # Initialize area as a class attribute

    def calculate_area(self):
        # local variable 'area' within the method
        area = self.l * self.w
        self.area = area  # Assign the local 'area' to the class attribute
        print(f"Area: {self.area}")

    def calculate_perimeter(self):
        # local variable 'p' within the method
        p = 2 * (self.l + self.w)
        print(f"Perimeter: {p}")

    def display(self):
        print(f"Length: {self.l}")
        print(f"Width: {self.w}")
        print(f"Area: {self.area}")
        # accessing the local variable 'p' from another method (calculate_perimeter) is not possible here

while True:
    try:
        length = float(input("Enter the length of the rectangle (or 'q' to quit): "))
        if length == 'q':
            break  # Exit the loop if user enters 'q'

        width = float(input("Enter the width of the rectangle: "))
        
        r = Rectangle(length, width)
        r.calculate_area()
        r.calculate_perimeter()
        r.display()
    except ValueError:
        print("Invalid input. Please enter a valid number for length and width.")

