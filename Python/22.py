# 22. Print Numbers Divisible by 'n': Implement a program that prints all numbers within a 
# certain range that are divisible by a given number 'n'.

def calculate(n):
    u=int(input("Enter Upperbound: "))
    l=int(input("Enter Lowerbound: "))
    for i in range(u,l+1):
        if(n%i==0):
            print(i)

n=int(input("Enter number to check divisibility: "))
calculate(n)