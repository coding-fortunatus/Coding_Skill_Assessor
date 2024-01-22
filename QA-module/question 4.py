"""
Write a program to design a grading system for your school and a program to compare between various numbers (Greatest, smallest) without using functions.
"""

# Grading System Program

# Get the marks from the user
marks = float(input("Enter the student's marks: "))

# Define the grading system
if marks < 0 or marks > 100:
    grade = "Invalid"
elif marks >= 75 and marks <= 100:
    grade = 'A'
elif marks >= 64 and marks <= 74:
    grade = 'B'
elif marks >= 55 and marks <= 65:
    grade = 'C'
elif marks >= 45 and marks <= 54:
    grade = 'D'
elif marks >= 40 and marks <= 44:
    grade = 'E'
else:
    grade = 'F'

# Display the grade
print(f"The student's grade is: {grade}")
