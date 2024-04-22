# 40. Display Fruits with Indices: Create a tuple named 'fruits' containing several fruit 
# names. Write a program that displays each fruit's name along with its index in the 
# tuple.
#q40
fruits=('Apple','mango','Bannana','Grapes','Kiwi')

for i in range(len(fruits)):
    print(f"{i}.{fruits[i]}")
