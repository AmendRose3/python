

odd_number = int(input("Enter an odd number: "))
range_limit = int(input("Enter the range limit: "))

if odd_number % 2 != 0:
    print("Odd multiples of", odd_number, "within the range are:")
    for i in range(1, range_limit+1):
        if i % 2 != 0 and i % odd_number == 0:
            print(i)
else:
    print("Input is not an odd number.")
