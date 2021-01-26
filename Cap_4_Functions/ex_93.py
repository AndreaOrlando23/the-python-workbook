# EXERCISE 93 : Center a string in the terminal window

WIDTH = 80


def center_string(s, width):
    if width < len(s):
        return s
    # Compute the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result


def main():
    word = input("Enter the word: ")

    while word != "":
        print(f"{center_string(word, WIDTH)}")
        word = input("Enter the word: ")


main()
