"""Write a Python program to implement a simple calculator (addition, subtraction, multiplication, division, and exponential) operations; using function and conditional statement where necessary.
"""

# Define the calculator operations


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def exponential(x, y):
    return x ** y

# Main calculator function


def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")

    choice = input("Enter choice (1-5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        elif choice == '5':
            result = exponential(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")
    else:
        print("Invalid choice")


# Call the calculator function
calculator()
