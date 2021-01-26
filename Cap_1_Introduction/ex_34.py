# EXERCISE 34 : Day old bread

LOAVES_PRICE = 3.49
DISCOUNT = 0.6

num_loaves = int(input('Enter the number of day old loaves: '))

regular_price = num_loaves * LOAVES_PRICE
purchase_discount = regular_price * DISCOUNT
total_price = regular_price - purchase_discount

print('Regular price: %5.2f' % regular_price)
print('Discount:      %5.2f' % purchase_discount)
print('Total:         %5.2f' % total_price)
