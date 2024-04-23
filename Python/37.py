# 37.	Record and Display Student Pairs for Projects: Write a Python program to manage student pairs for class projects. 
# The program should allow pairing two students, displaying all pairs, and exiting the program. 
# It should maintain a list of student pairs,
# where each pair is a tuple containing the names of the two students.

student_pairs = []

def pair_students():
    student_pairs = []

def pair_students():
    s1 = input("Enter name of student 1: ")
    s2 = input("Enter name of student 2: ")
    pair = (s1, s2)
    student_pairs.append(pair)
    print(f"{s1} and {s2} paired successfully.")

def display_pairs():
    print("Student Pairs:")
    for pair in student_pairs:
        print(f"{pair[0]} - {pair[1]}")

while True:
    print("\nStudent Pairing Program")
    print("1. Pair students")
    print("2. Display all pairs")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        pair_students()
    elif choice == "2":
        display_pairs()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
 