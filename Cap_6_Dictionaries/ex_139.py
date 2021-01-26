# EXERCISE 139 : Morse Code

character_to_code = {'A': '.-',
                     'B': '-...',
                     'C': '-.-.',
                     'D': '-..',
                     'E': '.',
                     'F': '..-.',
                     'G': '--.',
                     'H': '....',
                     'I': '..',
                     'J': '.---',
                     'K': '-.-',
                     'L': '.-..',
                     'M': '--',
                     'N': '-.',
                     'O': '---',
                     'P': '.--.',
                     'Q': '--.-',
                     'R': '.-.',
                     'S': '...',
                     'T': '-',
                     'U': '..-',
                     'V': '...-',
                     'W': '.--',
                     'X': '-..-',
                     'Y': '-.--',
                     'Z': '--..',
                     '0': '-----',
                     '1': '.----',
                     '2': '..---',
                     '3': '...--',
                     '4': '....-',
                     '5': '.....',
                     '6': '-....',
                     '7': '--...',
                     '8': '---..',
                     '9': '----.'}


def decode_morse(message):
    for char in message:
        for code in character_to_code:
            if char == code:
                print(character_to_code[code], end=" ")


def main():
    message = input("Enter your message: ").upper()
    decode_morse(message)


main()