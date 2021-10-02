# EXERCISE 46 : What color is that square (chess) - extended version with finctions

import string

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = list(string.ascii_lowercase)


def isInAlphabet(letter):
    if letter in alphabet:
        return True
    return False


def isDigit(value):
    if value.isdigit():
        return True
    return False


def evenOrodd(letterPosition, i):
    if (letterPosition + i) % 2 == 0:
        return True
    return False


def colorSquare():
    position = input("Please enter the chess board position (0 to exit): ")
    clean_input = position.replace(" ", "").lower()

    if clean_input == "0":
        quit()
    
    if isInAlphabet(clean_input[0]) and isDigit(clean_input[1:]):
        letterPosition = alphabet.index(clean_input[0])
        digit = int(clean_input[1:])
    else:
        print("Error: The position is not valid.")
        colorSquare()
    
    while clean_input:
        if evenOrodd(letterPosition, digit):
            print("White")
        else:
            print("Black")
        
        colorSquare()


colorSquare()
