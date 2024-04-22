#q8.
def swapnum(a,b):
    print("Before swapping")
    print("a = ",a)
    print("b = ",b)
    a,b=b,a
    print("After swapping")
    print("a = ",a)
    print("b = ",b)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number:"))
swapnum(num1,num2)
