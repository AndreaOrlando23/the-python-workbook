from ex_91 import ordinal_date


# EXERCISE 92 : Ordinal date to gregorian date
RETURN_PERIOD = 30

def is_leap_year(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    return False


def gregorian_date(day, year):
    day_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0

    if is_leap_year(year):
        day_per_months[1] = 29

    while (day - day_per_months[month]) > 0:
        day -= day_per_months[month]
        month += 1
        if month > len(day_per_months)-1:
            break
    return [day, month+1]  # return info to build gregorian date format (e.g. 1/1/2020)


def return_policy(day):
    return day + RETURN_PERIOD



def main():

    DAY = int(input("Enter the day number: "))
    MONTH = int(input("Enter the month number: "))
    YEAR = int(input("Enter the year: "))
    
    get_day = ordinal_date(DAY, MONTH, YEAR)  # return day whithin the year passed in gregorian date format (e.g. input: (25,2,2020) output: 56)
    set_return_day = return_policy(get_day)  # return the day + RETURN_PERIOD

    return_date = gregorian_date(set_return_day, YEAR)  # return [day, month] to build date in gregorian format (e.g. input: (56, 2020) output: [25, 2])
    if return_date[1] > 12:
        return_date[1] -= 12
        YEAR += 1
   
    print(f"You have to return the good on: {return_date[0]}/{return_date[1]}/{YEAR}")


if __name__ == "__main__":
    main()