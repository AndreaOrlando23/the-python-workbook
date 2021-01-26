from ex_133 import is_sublist

# EXERCISE 134 : Generate All Sublists of a List


def all_sublists(data):
    sublists = [[]]

    for length in range(1, len(data) + 1):
        print(length)
        for i in range(0, len(data) - length + 1):
            sublists.append(data[i:i + length])

    return sublists


def main():
    print("the sublists of [] are: ")
    print(all_sublists([]))

    print("the sublists of [1] are: ")
    print(all_sublists([1]))

    print("the sublists of [1, 2] are: ")
    print(all_sublists([1, 2]))

    print("the sublists of [1, 2, 3] are: ")
    print(all_sublists([1, 2, 3]))


main()