# EXERCISE 59 : Next day

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if year % 400 == 0:
    is_leap_year = True
elif year % 100 == 0:
    is_leap_year = False
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False

if day >= 31:
    if month == 1 or 3 or 5 or 7 or 8 or 10:
        day = 1
        month += 1
    else:
        day += 1
elif day >= 31:
    if month == 12:
        day = 1
        month = 1
        year += 1
    else:
        day += 1
elif day >= 30:
    if month == 4 or 6 or 9 or 11:  # April, June, September, November only have 30 days
        day = 1
        month += 1
    else:
        day += 1
elif is_leap_year:
    if day >= 29:
        if month == 2:
            day = 1
            month += 1
    else:
        day += 1
elif not is_leap_year:
    if day >= 28:
        if month == 2:
            day = 1
            month += 1
    else:
        day += 1

print(year, month, day)
