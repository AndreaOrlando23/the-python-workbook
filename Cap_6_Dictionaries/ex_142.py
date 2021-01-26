# EXERCISE 142 : Unique Characters


def histogram(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def unique_char(s):
    dictionary = histogram(s)
    unique_characters = 0
    for key in dictionary:
        if dictionary[key] == 1:
            unique_characters += 1
    return unique_characters


def main():
    s = input("Enter a string: ")
    result = unique_char(s)
    print(f"Your string has {result} unique characters")

# With this solution the program return in output only the letters that have 1 in dictionary
# If the letter appear twice (or more), the program will ignore it

# main()


# Solution by the book
s = input("Enter a string: ")
characters = {}

for ch in s:
    characters[ch] = 1

print(characters)
print(f"That string contained {len(characters)} unique character(s)")

