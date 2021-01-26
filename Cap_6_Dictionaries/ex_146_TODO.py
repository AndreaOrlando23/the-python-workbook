# EXERCISE 146 : Create a Bingo Card

from random import randrange


NUMS_PER_LETTER = 15


def create_card():
    card = dict()

    lower = 1
    upper = 1 + NUMS_PER_LETTER

    for letter in ["B", "I", "N", "G", "O"]:
        card[letter] = []

        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
            # Ensure that we do not include any duplicate numbers
            if next_num not in card[letter]:
                card[letter].append(next_num)

        # Update the range of values that will be generated for the next letter
        lower += NUMS_PER_LETTER
        upper += NUMS_PER_LETTER

    return card


def display_card(card):
    print("B  I  N  G  O")

    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d" % card[letter][i], end=" ")
        print()


def main():
    card = create_card()
    display_card(card)


if __name__ == '__main__':
    main()
