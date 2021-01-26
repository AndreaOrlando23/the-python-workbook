# EXERCISE 5 : Bottle deposit

LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

less = int(input('Enter the number of the container holding one liter or less: '))
more = int(input('Enter the number of the container holding more than one liter: '))
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

print('Your refund will be $%.2f' % refund)
