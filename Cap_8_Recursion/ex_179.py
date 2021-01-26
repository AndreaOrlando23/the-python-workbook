# EXERCISE 179 : Recursive Square Root
from math import sqrt


def square_root(n, guess=1.0):
    if abs(guess**2 - n) <= 10**-12:
        return guess
    else:
        guess = (guess + n/guess)/2
        return square_root(n, guess)


def main():
    num = float(input("Enter a number: "))
    result = square_root(num)
    print(f"Real root of {num} = {sqrt(num)}")
    print(f"Approximated root of {num} = {result}")


main()
