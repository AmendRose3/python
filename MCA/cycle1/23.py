# 23. Calculate Library Book Return Fine: Develop a program to calculate the fine for 
# returning a library book past the due date, based on the criteria provided.
def calculateDue():
    md = int(input("Enter Month of due(1-12): "))
    dd = int(input("Enter day of due(1-31): "))
    yd = int(input("Enter year of due: "))
    m = int(input("Enter Month (1-12): "))
    d = int(input("Enter day (1-31): "))
    y = int(input("Enter year: "))
    
    days = abs((yd - y) * 360 + (md - m) * 30 + (dd - d))

    print(f"Sorry you have {days} days due.")
    print(f"Per day due 3 rupees!")
    print(f"Total due amount: {days * 3} rupees")


calculateDue()
