# EXERCISE 175 : Recursive Decimal to Binary


def binary(n):
    if n < 0:
        return "Number must be a positive integer"
    elif n == 0:
        return "0"
    else:
        return binary(n//2) + str(n % 2)


def main():
    dec = int(input("Enter an integer: "))
    result = binary(dec)
    print(result)


main()
