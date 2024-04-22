def sort_dict_by_values(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict


num_students = int(input("Enter the number of students: "))
student_marks = {}
for i in range(num_students):
    student_name = input("Enter the name of student {}: ".format(i+1))
    student_mark = int(input("Enter the marks of student {}: ".format(i+1)))
    student_marks[student_name] = student_mark


sorted_student_marks = sort_dict_by_values(student_marks)


print("Sorted dictionary by marks:")
for name, mark in sorted_student_marks.items():
    print("Student:", name, ", Marks:", mark)
