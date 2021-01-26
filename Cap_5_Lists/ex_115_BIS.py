# List of Proper Divisors BIS


def divisors(n):
    proper_divisors = []

    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)

    return proper_divisors


def main():
    num = int(input("Enter a number: "))
    print(f"The proper divisors of {num} is/are: {divisors(num)}")


if __name__ == '__main__':
    main()