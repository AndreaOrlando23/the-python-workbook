# EXERCISE 176 : The Nato Alphabet

NATO_ALPHABET = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
                 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
                 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
                 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
                 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
                 'Z': 'Zulu'}


def check_phonetic(word):
    # Base Case
    if word == "":
        return ""

    # Recursive case
    spelling = ""
    letter = word[0]
    if letter in NATO_ALPHABET:
        spelling = spelling + NATO_ALPHABET[letter] + " " + check_phonetic(word[1:])
        print(word)

    return spelling


def main():
    word = input("Enter a word: ").upper()
    spelling = check_phonetic(word)
    print(spelling)


main()
