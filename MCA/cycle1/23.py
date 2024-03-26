# 23. Calculate Library Book Return Fine: Develop a program to calculate the fine for 
# returning a library book past the due date, based on the criteria provided.
17. Calculate Hourly-Based Salary: Implement a program to calculate an employee's salary
based on the number of hours worked and their hourly pay rate.

    m = int(input("Enter Month (1-12): "))
    d = int(input("Enter day (1-31): "))
    y = int(input("Enter year: "))
    
    days = abs((yd - y) * 360 + (md - m) * 30 + (dd - d))

    print(f"Sorry you have {days} days due.")
    print(f"Per day due 3 rupees!")
    print(f"Total due amount: {days * 3} rupees")


calculateDue()
