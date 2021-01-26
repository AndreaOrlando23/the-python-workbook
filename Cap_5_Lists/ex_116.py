# Perfect Numbers
from ex_115_BIS import divisors

limit = 10000


def perfect_numbers(n):
    # Find a proper divisors from i to n and store it in a list
    proper_divisors = divisors(n)

    if sum(proper_divisors) == n:
        return True
    return False


def main():
    for i in range(1, limit):
        if perfect_numbers(i):
            print(i)


main()