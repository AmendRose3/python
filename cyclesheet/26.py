#Q26
def intPalindrome(n):
    f=0
    a=n
    if a<0:     #removing the -ve sign
        a*=-1
        f=1
    rev=0
    while a!=0:
        r=a%10
        rev=rev*10+r
        a//=10
    if f==1:    #restoring the -ve sign
        rev*=-1
    if n==rev:
        print("Number is Palindrome")
    else:
        print("Not a Palindrome")

#main
num=int(input("Enter a number: "))
intPalindrome(num)
        
