#q7
import math as m
def getsqroot(n):
    if n<0:
        print("Invalid")
    else:
        print("Sqaure root of {} = {:.2f}".format(n,m.sqrt(n)))


n=float(input("Enter a number: "))
getsqroot(n)


        
