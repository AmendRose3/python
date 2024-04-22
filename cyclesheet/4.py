#Q4
def findArea(h,b):
    return 0.5*h*b

#main
print("To find the area of a triangle")
h=float(input("Enter height: "))
b=float(input("Enter base: "))
area=findArea(h,b)
print("Area = {:.2f} m2".format(area))