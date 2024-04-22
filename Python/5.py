import math
def area(r):
     a = math.pi * (r ** 2)
     return a

r = float(input("Radius: "))
area = area(r)
print(f"Area : {area}")