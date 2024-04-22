# 13. Convert Celsius to Fahrenheit: Implement a program that converts temperature from 
# Celsius to Fahrenheit.

import math
def convert(c):
     f = (c * 9/5) + 32
     return f

c = float(input("Celsius: "))
a = convert(c)
print(f"Fahrenheit : {a}")