# EXERCISE 88 : Median of three values - SOLUTION 2


def median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def main():
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = int(input("Enter the third value: "))

    print(f"The median value is: {median(x, y, z)}")


main()
