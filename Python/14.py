# 14. Convert Kilometers to Miles: Create a program to convert a distance from kilometers 
# to miles, using the conversion rate of 1.609 kilometers per mile.


def convert(km):
    miles = km / 1.609
    return miles

c = float(input("Kilometer: "))
a = convert(c)
print(f"Miles : {a}")
