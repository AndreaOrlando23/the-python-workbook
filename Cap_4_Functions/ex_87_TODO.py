# EXERCISE 87 : Shipping calculator

"""
Il programma sembra funzionare correttamente con tutti i valori passati tranne che per il 2
in quel caso l'output è 13.899999999...
--------chiedere su slack-----------------
"""

STANDARD_RATE = 10.95
PLUS_RATE = 2.95


def shipping(items):
    total_rate = (items - 1) * PLUS_RATE + STANDARD_RATE
    return total_rate


def main():
    order_items = int(input("Enter the number of items purchased: "))

    if order_items <= 1:
        print(f"The shipping rate is: {STANDARD_RATE}")

    else:
        total_shipping = shipping(order_items)
        print(f"The shipping rate is: {total_shipping}")


main()
