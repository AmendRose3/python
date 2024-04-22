#Q25
def findSum(n):
    s=0
    while n!=0:
        a=n%10
        s+=a
        n//=10
    return s

#main
n=int(input("Enter a number to find the sum of digits: "))
s=findSum(n)
print("Sum= ",s)
