'''Dictionary with tuples.
Print the topper(s) among ‘n’ students with Regno and marks of ‘m’ subjects.'''



def subject(n,m):
                   
                   for i in range(n):
                                       reg_no=input("Enter your registration number")
                                       subject=[]

                                       for j in range(m):
                                                          sub=int(input("Enter subject marks:"))
                                                          subject.append(sub)
                                       student_subject[reg_no]=tuple(subject)


                                       return student_subject

def topper(student_subject):
                            total_marks={ reg_no: sum(marks) for reg_no,marks in student_subject.items()}
                            highest= max(total_marks.values())
                            toppers= [reg_no for reg_no,total in total_marks.items() if total==highest]
                            return toppers

n= int(input("Enter number of student"))
m= int(input("Enter number of subjects"))
student_subject={}
student_subject=subject(n,m)
toppers=topper(student_subject)

print("toppers",','.join(toppers))

                                                           
