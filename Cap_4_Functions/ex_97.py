# EXERCISE 97 : Operator precedence


def precedence(operator):

    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3

    return -1


def main():
    operator = input("Enter the operator mark: ")
    print(precedence(operator))


if __name__ == '__main__':
    main()
