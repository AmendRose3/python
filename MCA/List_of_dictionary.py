def addpolicy():
    global deptnum, emp
    ename = input("Enter name: ")
    eage = int(input("Enter age: "))
    edept = input("Enter dept: ")
    
    if edept not in deptnum:
        deptnum[edept] = 0
    
    if deptnum[edept] < 3:
        newdict = {"name": ename, "age": eage, "dept": edept}
        emp.append(newdict)
        deptnum[edept] += 1
        print("Employee added successfully!")
    else:
        print("Department already has 3 staff. Re-enter.")


def printallemp(emp):
    avgage = 0
    for e in emp:
        print(e["name"])
        avgage += e["age"]
       
    avgage = avgage / len(emp)
    return avgage


deptnum = {"A": 2, "B": 1}
emp = [{"name": "Amend", "age": 21, "dept": "A"},
       {"name": "Rose", "age": 22, "dept": "A"},
       {"name": "Akkara", "age": 23, "dept": "B"}]

while True:
    print("Choose an option:")
    print("1. Add an employee")
    print("2. Print all employees")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        addpolicy()
    elif choice == "2":
        avgage = printallemp(emp)
        print("Average age of employees:", avgage)
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
