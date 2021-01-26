# EXERCISE 100 : Random Password
from random import randint


def random_password():
    min_length = 7
    max_length = 10
    random_length = randint(min_length, max_length)
    pw = ""

    for s in range(random_length):
        pw_char = chr(randint(33, 126))
        pw += pw_char
    return pw


def main():
    print(f"Your password is:\n{random_password()}")


if __name__ == '__main__':
    main()
