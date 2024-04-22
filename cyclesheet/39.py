#Q39
def setop(s1,s2):
    print("Union = ",s1|s2)
    print("Intersection = ",s1&s2)
    print("Difference (s1-s2) = ",s1-s2)
    print("Difference (s2-s1) = ",s2-s1)

#main
st1=input("Enter elements of Set A: ")
st2=input("Enter elements of Set B: ")
s1=set([i for i in st1.split()])
s2=set([i for i in st2.split()])
setop(s1,s2)