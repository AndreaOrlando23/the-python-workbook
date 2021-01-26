# EXERCISE 39 : Month name to number days

MONTHS_31 = 'january', 'march', 'may', 'july', 'august', 'october', 'december'
MONTHS_30 = 'november', 'april', 'june', 'september'
MONTHS_28 = 'february'

month = input('Enter one month: ').lower()

if month in MONTHS_28:
    print(f'The month {month} are 28 or 29 days.. it depends')
elif month in MONTHS_30:
    print(f'The month {month} are 30 days')
elif month in MONTHS_31:
    print(f'The month {month} are 31 days')
else:
    print(f'ERROR: the value entered is not a month')
