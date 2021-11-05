# EXERCISE 95 : Capitalize it
# not best solution - see ex_95_BIS


def capitalize(s):
    # Create a new copy of the string to return as the function's result
    result = s

    # Capitalize the first non-space character in the string
    pos = 0
    while pos < len(s) and result[pos] == ' ':
        pos += 1

    if pos < len(s):
        # Replace the character with its uppercase version without changing any other characters
        result = result[0:pos] + result[pos].upper() + result[pos + 1:len(result)]

    # Capitalize the first letter that follows a ".", "!" or "?"
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            # Move past the ".", "!" or "?"
            pos += 1

            # Move past any spaces
            while pos < len(s) and result[pos] == " ":
                pos += 1

            # If we haven't reached the end of the string then replace the current character
            # with its uppercase equivalent
            if pos < len(s):
                result = result[0:pos] + result[pos].upper() + result[pos + 1:len(result)]

        # Move the next character
        pos += 1

        # Capitalize "i" when it is preceded by a space and followed by a space, period, exclamation mark,
        # question mark or apostrophe
        pos = 1
        while pos < len(s) - 1:
            if result[pos - 1] == " " and result[pos] == "i" and \
                    (result[pos + 1] == " " or result[pos + 1] == "." or
                     result[pos + 1] == "!" or result[pos + 1] == "?" or
                     result[pos + 1] == "'"):
                # Replace the "i" with an "I" without changing any other characters
                result = result[0:pos] + "I" + result[pos + 1:len(result)]

            pos += 1

        return result


def main():
    s = input("Enter some text: ")
    capitalized = capitalize(s)
    print(f"It is capitalized as:\n{capitalized}")


# what time do i have to be there? what's the address? this time i'll try to be on time! i promise
main()
