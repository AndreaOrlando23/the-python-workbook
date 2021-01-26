# EXERCISE 15 : Distance Units

IN_PER_FT = 12
YARDS_PER_FT = 0.333333
MILES_PER_FT = 0.000189394

distance = int(input('Enter the distance in feet: '))

print('The equivalent distance in inches is: ', distance * IN_PER_FT)
print('The equivalent distance in yards is: %.2f' % (distance * YARDS_PER_FT))
print('The equivalent distance in miles is: ', distance * MILES_PER_FT)
