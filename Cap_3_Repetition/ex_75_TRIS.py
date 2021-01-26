# EXERCISE 75 : Is a string a palindrome? - SOLUTION 3 (book)

line = input("Enter a string: ").lower()

# Assume that it is a palindrome until we can prove otherwise
is_palindrome = True

# Check the characters, starting from the ends. Continue until the middle is reached or we have
# determined that the string is not a palindrome.
i = 0
while i < len(line) / 2 and is_palindrome:
    # If the character do not match then mark that the string is not a palindrome
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False

    # Move to the next character
    i += 1

if is_palindrome:
    print(f"{line} is a palindrome")
else:
    print(f"{line} is not a palindrome")
