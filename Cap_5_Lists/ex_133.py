# EXERCISE 133 : Does a List Contain a Sublist


def is_sublist(larger, smaller):
    sub_set = False
    if len(smaller) == 0:
        sub_set = True
    elif smaller == larger:
        sub_set = True
    elif len(smaller) > len(larger):
        sub_set = False

    else:
        for i in range(len(larger)):
            if larger[i] == smaller[0]:
                n = 1
                while (n < len(smaller)) and (larger[i + n] == smaller[n]):
                    n += 1

                if n == len(smaller):
                    sub_set = True

    return sub_set


def main():
    a = [2, 4, 3, 5, 7]
    b = [4, 3, 5]
    c = [3, 7]
    print(is_sublist(a, b))
    print(is_sublist(a, c))


main()

