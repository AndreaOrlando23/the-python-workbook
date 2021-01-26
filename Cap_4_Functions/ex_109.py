# EXERCISE 109 : Magic dates
from ex_106 import leap_year

# From exercise 106
"""def leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False"""


def days_in_month(month, year):
    if 1 >= month >= 12:
        print("Error")
        quit()

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28


def is_magic_date(day, month, year):
    if day * month == year % 100:
        return True

    return False


# Find and display all of the magic dates in 1900s
def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                if is_magic_date(day, month, year):
                    print(f"{day}/{month}/{year} is a magic date")


main()
