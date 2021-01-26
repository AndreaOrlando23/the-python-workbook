# EXERCISE 130 : Unary and Binary Operators

from ex_129 import token_list


def identify_unary(tokens):
    retval = []

    for i in range(len(tokens)):
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])

        elif i > 0 and (tokens[i] == "+" or tokens[i] == "-") and \
                (tokens[i-1] == "+" or tokens[i-1] == "-" or tokens[i-1] == "*" or tokens[i-1] == "/" or tokens[i-1] == "("):
            retval.append("u" + tokens[i])
        else:
            retval.append(tokens[i])

    return retval


def main():
    exp = input("Enter a mathematical expression: ")
    tokens = token_list(exp)
    print(f"The tokens are: {tokens}")

    marked = identify_unary(tokens)
    print(f"With unary operators marked: {marked}")


if __name__ == '__main__':
    main()