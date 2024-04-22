def findFact(n):
    if n<0:
        return -1
    elif n==0:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f*=i
        return f

#main
n=int(input("Enter a number to find its factorial: "))
fac=findFact(n)
if fac!=-1:
    print("Factorial = ",fac)
else:
    print("Not defined!")