if __name__ == "__main__":
    # Get user input to create instances of each subclass
    name = input("Enter Full Time Employee's Name: ")
    emp_id = input("Enter Full Time Employee's ID: ")
    department = input("Enter Full Time Employee's Department: ")
    monthly_salary = float(input("Enter Full Time Employee's Monthly Salary: "))
    full_time_emp = FullTimeEmployee(name, emp_id, department, monthly_salary)

    name = input("\nEnter Part Time Employee's Name: ")
    emp_id = input("Enter Part Time Employee's ID: ")
    department = input("Enter Part Time Employee's Department: ")
    hours_worked = float(input("Enter Part Time Employee's Hours Worked: "))
    hourly_rate = float(input("Enter Part Time Employee's Hourly Rate: "))
    part_time_emp = PartTimeEmployee(name, emp_id, department, hours_worked, hourly_rate)

    name = input("\nEnter Freelance Employee's Name: ")
    emp_id = input("Enter Freelance Employee's ID: ")
    department = input("Enter Freelance Employee's Department: ")
    projects_completed = int(input("Enter Freelance Employee's Projects Completed: "))
    rate_per_project = float(input("Enter Freelance Employee's Rate per Project: "))
    freelance_emp = FreelanceEmployee(name, emp_id, department, projects_completed, rate_per_project)

    # Display details for each employee
    print("\nFull Time Employee Details:")
    full_time_emp.display_details()
    print("\nPart Time Employee Details:")
    part_time_emp.display_details()
    print("\nFreelance Employee Details:")
    freelance_emp.display_details()
