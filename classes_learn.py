
#we  use classes to defne new types 
class Point:
    # We also have a constructor here.
    # Self is the reference to the current object.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self):
        print(f"move {self.x}")

    def draw(self):
        print(f"draw {self.y}")

# We can create objects.
p1 = Point()
# We can define attributes of the class anywhere.
p1.x = 10
print(p1.x)
p1.draw()
p1.move()

p2 = Point()
p2.x = 20
print(p2.x)
p2.draw()
p2.move()

# Call the constructor with values.
p3 = Point(30, 40)
print(p3.x, p3.y)
p3.draw()
p3.move()
