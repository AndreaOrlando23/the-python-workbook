# EXERCISE 138 : Text Messaging

keys_symbols = {1: ['.', ',', '?', '!', ':'],
                2: ['A', 'B', 'C'],
                3: ['D', 'E', 'F'],
                4: ['G', 'H', 'I'],
                5: ['J', 'K', 'L'],
                6: ['M', 'N', 'O'],
                7: ['P', 'Q', 'R', 'S'],
                8: ['T', 'U', 'V'],
                9: ['W', 'X', 'Y', 'Z'],
                0: [' ']}


def message(text):
    for letter in text:
        for key in keys_symbols:
            if letter in keys_symbols[key]:
                print(key, end="")


def main():
    sms = input("Enter your message: ").upper()
    message(sms)


main()
