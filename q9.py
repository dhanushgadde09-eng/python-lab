# Student Grading System

students = []

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"


output
 Enter number of students: 4

Student 1
Enter student name: ram
Enter marks out of 100: 85

Student 2
Enter student name: raj
Enter marks out of 100: 65

Student 3
Enter student name: umesh
Enter marks out of 100: 45

Student 4
Enter student name: yash
Enter marks out of 100: 32

--- Student Results ---
ram - Marks: 85.0 - Grade: A
raj - Marks: 65.0 - Grade: C
umesh - Marks: 45.0 - Grade: F
yash - Marks: 32.0 - Grade: F

    students.append({"name": name, "marks": marks, "grade": grade})

print("\n--- Student Results ---")
for student in students:
    print(student["name"], "- Marks:", student["marks"], "- Grade:", student["grade"])
