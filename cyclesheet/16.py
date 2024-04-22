#Q16
def eligibilityTest(first,marks):
    s=0
    for i in marks:
        if i<=0:                 #checking valid marks
            print("Invalid marks")
            return
        else:
            s+=i
    avg=s/3                 #calculating average
    print("Average= {:.2f}".format(avg))
    if first==1 and avg>98:
        print("Eligible for scholarship")
    else:
        print("Not Eligible")

#main
f=int(input("Enter 1 if candidate is first graduate in their family, else 0 if not: "))
l=[]
l.append(float(input("Enter marks in math:")))
l.append(float(input("Enter marks in physics:")))
l.append(float(input("Enter marks in chemistry:")))
eligibilityTest(f,l)
