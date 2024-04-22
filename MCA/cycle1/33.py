def perfectsqcheck(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci(num):
    # A number is Fibonacci if and only if one or both of (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square
    return perfectsqcheck(5 * num * num + 4) or perfectsqcheck(5 * num * num - 4)

# Test the function
number = int(input("Enter a number to check:  "))
if is_fibonacci(number):
    print(number, "is part of the Fibonacci sequence.")
else:
    print(number, "is not part of the Fibonacci sequence.")
