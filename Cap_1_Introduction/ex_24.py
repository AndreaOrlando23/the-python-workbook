# EXERCISE 24 : Units of time

D = int(input('Enter the number of days: '))
H = int(input('Enter the hours: '))
M = int(input('Enter the minutes: '))
S = int(input('Enter the seconds: '))

days_in_seconds = D * 24 * 60 ** 2
hours_in_seconds = H * 60 ** 2
minutes_in_seconds = M * 60

print('The amount duration in seconds is: ', days_in_seconds + hours_in_seconds + minutes_in_seconds + S)
