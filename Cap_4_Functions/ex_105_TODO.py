# EXERCISE 105 : Arbitrary base conversions
# TODO


def base_check(base):
    if 2 <= base <= 16:
        return True
    return False


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def main():
    base = int(input("Chose the base (2 to 16): "))
    if not base_check(base):
        print("ERROR: Please chose a valid base")
        main()
    num = int(input("Enter a number: "))
    print(numberToBase(num, base))

if __name__ == '__main__':
    main()


