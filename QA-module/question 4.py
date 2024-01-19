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

# Number Comparison Program

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Display the results
print(f"The greatest number is: {greatest}")
print(f"The smallest number is: {smallest}")
