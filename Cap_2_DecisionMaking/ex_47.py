# EXERCISE 47 : Season from month and day

month = input("Enter the month of your birthday: ").lower()
day = int(input("Enter the day of your birthday: "))
season = ""

if month == "january" or month == "february":
    season = "Winter"
elif month == "march":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "april" or month == "may":
    season = "Spring"
elif month == "june":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "july" or month == "august":
    season = "Spring"
elif month == "september":
    if day < 22:
        season = "Spring"
    else:
        season = "Fall"
elif month == "october" or month == "november":
    season = "Fall"
elif month == "december":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"

print(month, day, "is in", season)
