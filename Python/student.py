''' Store and Display Top-Scoring Student Details: Design a Python program to store details of students
including their registration number, name, and marks in three subjects. The program should be able to identify and
display the details of the student or students who have achieved the highest total mark.'''




student_details={}
n=int(input("Enter number of student"))
def details(n):
                   for i in range(n):
                       reg_no=input("Enter registration number")
                       details=[]
                       for i in range(2):

                                           name=input("Enter your name")
                                           details.append(name)
                                           marks=[]
                                           for i in range(3):
                                                               mark=int(input("Enter marks in sub"))
                                                               marks.append(mark)
                                           details.append(marks)
                                           total=marks[0]+marks[1]+marks[2]
                                           details.append(total)
                                           return  student_details


def high(student_details):
                                max_score=-1
                                high_scorer=" "
                                topper=[]
                                for total in student_details.values():

                                                                          if(total>max_score):
                                                                                              max_score=total
                                                                                              high_scorer=name
                                                                                              topper.append(max_score,high_score)

                                                                                              print("Toppers",",".join(topper))
                                                                                              print(max_score)

                                                                                        
student_details=details(n)
high(student_details)


                                                                                   
                                                                                   
                                                                                   
                           



                              
      
                                                       
