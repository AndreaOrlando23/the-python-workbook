# EXERCISE 14 : Height Units

IN_PER_FT = 12
CM_PER_IN = 2.54

print('enter your height:')

feet = int(input(' Number of feet: '))
inches = int(input(' Number inches: '))

cm = (feet * IN_PER_FT + inches) * CM_PER_IN

print('Your height in centimeters is:', cm)
