# EXERCISE 45 : Date to holiday name

NEW_YEAR_MONTH = "january"
NEW_YEAR_DAY = 1

CANADA_MONTH = "july"
CANADA_DAY = 1

CHRISTMAS_MONTH = "december"
CHRISTMAS_DAY = 25

month = input("Enter the month: ").lower()
day = int(input("Enter the day: "))

if month == NEW_YEAR_MONTH and day == NEW_YEAR_DAY:
    print("That's new year's day!")
elif month == CANADA_MONTH and day == CANADA_DAY:
    print("That's Canada's day!")
elif month == CHRISTMAS_MONTH and day == CHRISTMAS_DAY:
    print("Marry Christmas!")
else:
    print("Is not holiday time :(")

