# EXERCISE 153 : Find the longest word in a file

f_name = input("Enter the name of the file: ")


def longest_word(file_name):
    inf = open(file_name, "r")
    lines = inf.read().splitlines()
    longest = []
    length = 0

    for word in lines:
        if len(word) > length:
            longest = [word]
            length = len(word)
        elif len(word) == length:
            if word not in longest:
                longest.append(word)

    print(longest)


longest_word(f_name)
