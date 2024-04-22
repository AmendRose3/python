

def add_complex(a, b):
    return a + b

def subtract_complex(a, b):
    return a - b

def multiply_complex(a, b):
    return a * b

real1 = float(input("Enter real part of first complex number: "))
imaginary1 = float(input("Enter imaginary part of first complex number: "))
real2 = float(input("Enter real part of second complex number: "))
imaginary2 = float(input("Enter imaginary part of second complex number: "))

complex1 = complex(real1, imaginary1)
complex2 = complex(real2, imaginary2)

operation = input("Enter the operation to perform (+ for addition, - for subtraction, * for multiplication): ")

if operation == '+':
    result = add_complex(complex1, complex2)
    print("Result:", result)
elif operation == '-':
    result = subtract_complex(complex1, complex2)
    print("Result:", result)
elif operation == '*':
    result = multiply_complex(complex1, complex2)
    print("Result:", result)
else:
    print("Invalid operation!")
