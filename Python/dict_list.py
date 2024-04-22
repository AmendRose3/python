'''Dictionary of List
Develop a Python script to organize student course registrations. Use a dictionary mapping student IDs to
their registered courses.
student_courses = {"23MCA0001": ["Python", "Operating Systems"]}
Operations:
1.
Add Registration: Add a course for a student by updating the dictionary. Create a new entry if the student ID is new.
2.
Display Registrations: Print all students with their courses.
3.
Query Courses: Given a student ID, show their courses or indicate if the ID is not found.'''

print("Menu:")
print("1.Add a registration")
print("2.Display registration")
print("3.Display courses ")

student_courses={}
while True:
           choice=int(input("Enter your choice"))
           if choice== 1:
                          student_id=input("Enter student_id:")
                          student_course=input("Enter your course")
                          if student_id in student_courses:
                                                           student_courses[student_id].append(student_course)
                          else:
                                                           student_courses[student_id]=student_course

           elif choice==2:
                          print("Display student registration")
                          for student_id, student_course in student_courses.item():
                                                                                    print(f"Student id {student_id} and Courses {student_course}")

           elif choice==3:
                           print("Display courses")
                           student_id=input("Enter student id:")
                           if student_id in student_courses:
                                                             print(f"Courses : {','.join(student_course[student_id])}")
                           else:
                                                             print("Not found")

           elif choice==4:
                           print("Enter valid input")
                           break


           else:
                  print("Enter valid input")
                                                                                 
                                                                                 
                     
