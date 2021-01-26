# EXERCISE 174 : Greatest Common Divisor


def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)


def main():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))

    result = gcd(number_1, number_2)
    print(result)


main()
