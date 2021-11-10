# EXERCISE 99 : Next Prime


from ex_98 import is_prime


def next_prime(n):
    # Use the function from exercise 98
    next_n = n + 1  # if n is already prime, go to the next n and find the next prime
    while not is_prime(next_n):
        next_n += 1
        is_prime(next_n)
    return next_n


def main():
    value = int(input("Enter a number: "))
    print(f"The next prime number is: {next_prime(value)}")


main()
