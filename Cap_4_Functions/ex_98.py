# EXERCISE 98 : Is a prime number?


def is_prime(n):
    if n < 0:
        print("ERROR")
        quit()

    elif n <= 2:
        return True

    """
    Check each number from 3 up to but not including n to see if it divides evenly into n
    if n % i == 0 then n is evenly divisible by i, indicating that n is not prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def main():
    value = int(input("Enter the value: "))
    if is_prime(value):
        print(f"{value} is prime")
    else:
        print(f"{value} is not prime")


if __name__ == '__main__':
    main()
