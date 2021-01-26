# EXERCISE 64 : Discount table

purchase = [4.95, 9.95, 14.95, 19.95, 24.95]

for values in purchase:
    regular_price = values
    discount = values * 60 / 100
    net_price = regular_price - discount

    print('-' * 25)
    print(f"Regular price:\t {regular_price} €\nDiscount:\t\t %.2f €\nNew price:\t\t %.2f €" % (discount, net_price))
    print('-' * 25)

