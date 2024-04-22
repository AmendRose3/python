#Q27
def strPalindrome(s):
    rev=s[::-1]
    if s==rev:
        print("String is Palindrome")
    else:
        print("Not a Palindrome!!")

#main
s=input("Enter a string: ")
strPalindrome(s)
    
