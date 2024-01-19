"""
Implement a Python program that counts the occurrences of each letter in a given text and prints the result without using functions
"""

# Input text
text = input("Enter a text: ")

# Initialize a dictionary to store letter occurrences
letter_counts = {}

# Count occurrences of each letter
for char in text:
    if char.isalpha():
        char = char.lower()  # Convert to lowercase to treat 'A' and 'a' as the same letter
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# Display results
print("Letter occurrences:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
