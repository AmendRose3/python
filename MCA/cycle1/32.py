# 32. List Fibonacci Numbers in a Range: Develop a program to generate and display the 
# Fibonacci numbers within a specified range.

def Fibonacci(u):
    a, b = 0, 1
    print(a, end=" ") 
    while b <= u:
        print(b, end=" ")  
        a, b = b, a + b




u = int(input("Upperbound:"))
Fibonacci(u)