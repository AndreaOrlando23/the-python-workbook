# EXERCISE 58 : Is it a leap year?

year = int(input("Enter the year: "))

if year % 400 == 0:
    is_leap_year = True
elif year % 100 == 0:
    is_leap_year = False
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
