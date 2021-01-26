# EXERCISE 96 : Does the string represent an integer?


def is_integer(s):
    # Remove white space from the beginning and end of the string
    s = s.strip()

    """
    Determine if the remaining characters form a valid integer
    The isdigit method returns True if and only if the string is at least one character in length
    and all of the characters in the string are digits
    """
    if (s[0] == '+' or s[0] == '-') and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False


def main():
    s = input("Enter a string: ")

    if is_integer(s):
        print("That string represents an integer")
    else:
        print("That string does not represent an integer")


# Only call the main function when this file has not been imported
if __name__ == '__main__':
    main()
