# EXERCISE 106 : Days in a month


def leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


def days_in_month(month, year):
    if 1 >= month >= 12:
        print("Error")
        quit()

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("This month have 31 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("This month have 30 days")
    elif month == 2:
        if leap_year(year):
            print("This month have 29 days")
        else:
            print("This month have 28 days")


def main():
    month = int(input("Enter the month in digit number: "))
    year = int(input("Enter the year: "))

    days_in_month(month, year)


main()
