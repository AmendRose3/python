

subject1 = float(input("Enter marks obtained in subject 1: "))
subject2 = float(input("Enter marks obtained in subject 2: "))
subject3 = float(input("Enter marks obtained in subject 3: "))

average_marks = (subject1 + subject2 + subject3) / 3

if average_marks >= 65:
    print("Congratulations! You have passed with an average of", average_marks)
else:
    print("Sorry! You have failed with an average of", average_marks)
