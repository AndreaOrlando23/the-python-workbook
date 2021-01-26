# EXERCISE 177 BIS : Roman Numerals
# TODO

numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_numeral(roman_number):
    for char in roman_number:
        if char in numerals:
            return numerals[char]

        else:
            if roman_to_numeral(roman_number[0]) < roman_to_numeral(roman_number[1]):
                return (roman_to_numeral(roman_number[1]) - roman_to_numeral(roman_number[0])) + roman_to_numeral(roman_number[2:])
            else:
                return roman_to_numeral(roman_number[0]) + roman_to_numeral(roman_number[1:])


def main():
    n = input("Enter a number: ")
    result = roman_to_numeral(n)
    print(f"The conversion of {n} in roman is: {result}")


main()