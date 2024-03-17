# 4. Calculate Area of a Triangle: Implement a program that calculates the area of a triangle 
# given its base and height
def area(b, h):
    a = 0.5 * b * h
    return a

b = float(input("base: "))
h = float(input("height: "))
area = area(b, h)
print(f"Area : {area}")