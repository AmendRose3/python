# 6. Calculate Area of a Rectangle: Develop a program to find the area of a rectangle using 
# its length and breadth

def area(l, b):
    a = l * b
    return a

l = float(input("length: "))
b = float(input("breadth: "))
area = area(l, b)
print(f"Area : {area}")