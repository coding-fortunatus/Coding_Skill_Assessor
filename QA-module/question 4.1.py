"""
Write a program to compare between various numbers (Greatest, smallest) without using function.
"""


# Number of elements
digit = int(input("Enter the number of elements: "))

# Initialize variables
greatest = None
smallest = None

# Input numbers
for i in range(digit):
    num = float(input(f"Enter number {i + 1}: "))

    # Check for greatest and smallest
    if greatest is None or num > greatest:
        greatest = num
    if smallest is None or num < smallest:
        smallest = num

# Display results
print(f"The greatest number is: {greatest}")
print(f"The smallest number is: {smallest}")
