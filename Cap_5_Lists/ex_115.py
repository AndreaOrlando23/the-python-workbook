# List of Proper Divisors


def divisors(n):
    proper_divisors = []

    # Parse the number from 1 to n+1 to include n as its own divisor
    for i in range(1, n+1):
        if n % i == 0:
            proper_divisors.append(i)

    print(f"The proper divisors of {n} is/are: {proper_divisors}")


def main():
    num = int(input("Enter a number: "))
    divisors(num)


if __name__ == '__main__':
    main()

