class Robot:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def intro(self):
        print("Robot name is " + self.name)
        print("Robot color is " + self.color)
class Person:
    def __init__(self,name,robotown,isSitting):
        self.name=name
        self.robotown=robotown
        self.isSitting=isSitting


    def sit_down(self):
        self.isSitting=True

    def stand_up(self):
        self.isSitting=False


r1=Robot('Tom','green')
r2=Robot('Sara','Blue')

//pass object r1,r2 as parameter
p1=Person("Amend",r1,True)
p2=Person("Daniel",r2,False)

print(p1.robotown.name)

# r1.intro()
# r2.intro()



