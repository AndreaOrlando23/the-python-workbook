# EXERCISE 186 : Run-Length Encoding


def compression(data):

    if len(data) == 0:
        return []

    index = 1
    while len(data) > index and data[index] == data[index-1]:
        index += 1

    current = [data[0], index]

    return current + compression(data[index:len(data)])


def main():
    my_list = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'E', 'E', 'E', 'E', 'E']
    result_list = compression(my_list)
    result_string = compression("aaaaaabbbbbbbcccccccdddddd")

    print(result_list)
    print(result_string)


main()
