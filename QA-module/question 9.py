"""
Write a Python program to open a file in read-only mode and print its contents using with statements
"""


def is_leap_year(year):
    """
    Check if a year is a leap year.

    :param year: The year to be checked.
    :return: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Example: Check if the year 2024 is a leap year
year_to_check = 2024

if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
