# 5. Calculate Area of a Circle: Write a program to compute the area of a circle, using the 
# radius provided by the user.

import math
def area(r):
     a = math.pi * (r ** 2)
     return a

r = float(input("Radius: "))
area = area(r)
print(f"Area : {area}")