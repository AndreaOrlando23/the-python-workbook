# EXERCISE 177 : Roman Numerals

numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def integer_to_roman(number):
    flag = None
    for symbol, integer in numerals.items():
        if integer == number:
            return symbol
        if number > integer:
            flag = symbol

    remaining = number - numerals[flag]
    return flag + integer_to_roman(remaining)


def main():
    n = int(input("Enter a number: "))
    result = integer_to_roman(n)
    print(f"The conversion of {n} in roman is: {result}")


main()