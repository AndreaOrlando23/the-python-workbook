# EXERCISE 186 : Run-Length Decoding


def decompression(data):

    if len(data) == 0:
        return []

    else:
        result = data[0] * data[1]
        return list(result) + decompression(data[2:])


def main():
    data = ['A', 3, 'B', 2, 'C', 6, 'D', 1, 'E', 5]
    result = decompression(data)
    print(result)


main()