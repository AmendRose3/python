def calculate_total_marks(marks):
    return sum(marks)

def find_top_scoring_students(student_details):
    top_score = max(student_details, key=lambda x: student_details[x]['total_marks'])
    top_score_value = student_details[top_score]['total_marks']
    top_students = [student for student in student_details if student_details[student]['total_marks'] == top_score_value]
    return top_students, top_score_value


num_students = int(input("Enter the number of students: "))
student_details = {}
for i in range(num_students):
    reg_number = input("Enter registration number of student {}: ".format(i+1))
    name = input("Enter name of student {}: ".format(i+1))
    marks = [int(input("Enter marks for subject {}: ".format(j+1))) for j in range(3)]
    total_marks = calculate_total_marks(marks)
    student_details[reg_number] = {'name': name, 'marks': marks, 'total_marks': total_marks}


top_students, top_score = find_top_scoring_students(student_details)


print("\nTop Scoring Student(s) with Total Marks:", top_score)
for student in top_students:
    print("Registration Number:", student)
    print("Name:", student_details[student]['name'])
    print("Marks:", student_details[student]['marks'])
    print()
