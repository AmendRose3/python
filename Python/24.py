# 24. Calculate Factorial of a Number: Write a program to calculate the factorial of a given 
# number 'n'.

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact



m = int(input("Enter a number to find factorial: "))
print(factorial(m))