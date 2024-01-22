"""
Implement the Fizzbuzz problem using a while loop. Print numbers from 1 to and end range, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for numbers that are multiples of both 3 and 5, print "Fizzbuzz without function."
"""

# Initialize the counter
number = 1
end_range = int(input("Enter end range: "))
# Loop through numbers 1 to 20
while number <= 20:
    # Check for multiples of both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check for multiples of 3
    elif number % 3 == 0:
        print("Fizz")
    # Check for multiples of 5
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

    # Increment the counter
    number += 1
