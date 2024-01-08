#While loop
s = 7
guesstimes = 1
print("Let's begin")

while guesstimes < 4:
    guess = int(input("Enter your guess: "))

    if guess == s:
        print("Correct guess")
        print("YOU WON")
        break
    else:
        print("Wrong guess")

    guesstimes += 1

if guesstimes > 3:
    print("YOU LOSE")

print("Thank you for playing")
