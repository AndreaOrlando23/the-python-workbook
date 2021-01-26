# EXERCISE 99 : Next Prime
# TODO

from ex_98 import is_prime


def next_prime(n):
    # Use the function from exercise 98
    while not is_prime(n):
        n += 1
        is_prime(n)
    return n


def main():
    value = int(input("Enter the value: "))
    print(next_prime(value))


main()
