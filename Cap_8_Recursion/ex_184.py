# EXERCISE 184 : Flatten a list


def flattening(data):

    if len(data) == 0:
        return []

    if type(data[0]) == list:
        l1 = flattening(data[0])
        l2 = flattening(data[1:])
        return l1 + l2

    if type(data[0]) != list:
        l1 = [data[0]]
        l2 = flattening(data[1:])
        return l1 + l2


def main():
    sample_list = [1, [2, 3], [4, [5, [6, 7]]], [[8], 9], [10]]
    result = flattening(sample_list)

    print(result)


main()