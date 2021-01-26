# EXERCISE 107 : Reduce a fraction to lowest terms


def gcd(m, n):
    # Initialize d to the smaller of n and m
    d = min(m, n)

    # Use a while loop to find the greatest common divisor of n and m
    while n % d != 0 or m % d != 0:
        d -= 1

    return d


def reduce(num, den):
    # If the numerator is 0 then the reduced fraction is 0/1
    if num == 0:
        return 0, 1

    # Compute the greatest common divisor of the numerator and denominator
    g = gcd(num, den)

    # Divide both the numerator and denominator by the GCD and return the result
    return num // g, den // g


def main():

    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    # Compute the reduced fraction
    (n, d) = reduce(num, den)

    print(f"{num}/{den} can be reduced to {n}/{d}")


main()
