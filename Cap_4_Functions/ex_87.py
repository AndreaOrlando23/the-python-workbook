# EXERCISE 87 : Shipping calculator

STANDARD_RATE = 10.95
PLUS_RATE = 2.95


def shipping(items):
    total_rate = (items -1) * PLUS_RATE + STANDARD_RATE
    return total_rate


def main():
    order_items = int(input("Enter the number of items purchased: "))

    if order_items <= 1:
        print(f"The shipping rate is: {STANDARD_RATE}")

    else:
        # round() is a workaround in case the order_items == 2
        # couse of the output of 2.95 + 10.95 generate the result of 13.899999999999999 instead of 13.9
        # all the others cases works fine
        total_shipping = round(shipping(order_items), 2)
        print(f"The shipping rate is: {total_shipping}")


main()
