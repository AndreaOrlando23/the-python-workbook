# EXERCISE 9 : Compound interest

INTEREST = 0.04

deposit = float(input('Enter your deposit amount: '))
first_year = deposit * INTEREST
deposit1 = deposit + first_year
second_year = deposit1 * INTEREST
deposit2 = deposit1 + second_year
third_year = deposit2 * INTEREST
deposit3 = deposit2 + third_year

print('The amount of your savings account after one year is $%.2f' % deposit1)
print('after two years is $%.2f' % deposit2)
print('and after three years is $%.2f' % deposit3)
