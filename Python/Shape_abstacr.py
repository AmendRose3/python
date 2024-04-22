from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __area__(self):
        pass

    @abstractmethod
    def __peri__(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def __area__(self):
        a = 3.14 * self.r * self.r
        print(f"Area: {a}")

    def __peri__(self):
        p = 2 * 3.14 * self.r
        print(f"Perimeter: {p}")

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        a = self.s * self.s
        print(f"Square Area: {a}")

    def perimeter(self):
        p = 4 * self.s
        print(f"Square Perimeter: {p}")

obj = []
for i in range(3):
    obj.append(Circle(0))

while True:
    o = int(input("Enter object number: "))
    c = int(input("1. Area 2. Perimeter 3. End: "))
    r = int(input("Enter Radius: "))

    if c == 1:
        obj[o].__area__()
    elif c == 2:
        obj[o].__peri__()
    elif c == 3:
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
