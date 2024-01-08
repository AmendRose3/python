import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(1,20))

name=["Amend","Leo","Amstin","Geo","Jees","Jinu","stemin"]
chosen=random.choice(name)
print(chosen)