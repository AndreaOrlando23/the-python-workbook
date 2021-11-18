# EXERCISE 6 : Tax and Tip

TAX_RATE = 10
TIP_RATE = 18

meal = float(input('Enter the cost of tour meal: '))
tax_amount = meal * TAX_RATE / 100
tip_amount = meal * TIP_RATE / 100
total_amount = meal + tax_amount + tip_amount

print('The tax amount is $%.2f and the tip is $%.2f, making the total $%.2f' % (tax_amount, tip_amount, total_amount))
