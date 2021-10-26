# EXERCISE 91 : Gregorian date to ordinal date

def is_leap_year(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    return False


def ordinal_date(day, month, year):
    day_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check if year is actually a leap year or not
    if is_leap_year(year):
        day_per_months[1] = 29
        result = day + sum(day_per_months[:month-1])
    else:
        # if not a leap year compute directly from the original list day_per_months
        result = day + sum(day_per_months[:month-1])
    
    return result


def main():
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    result = ordinal_date(day, month, year)

    print(f"Gregorian date: {day}/{month}/{year} corrispond at the ordinal date: {result}/{year}")


if __name__ == "__main__":
    main()