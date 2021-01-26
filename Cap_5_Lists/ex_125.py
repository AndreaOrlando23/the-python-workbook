# EXERCISE 125 : Shuffling a Deck Cards

from random import randrange


def create_deck():
    cards = []
    suits = ["s", "h", "d", "c"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]

    for suit in suits:
        for value in values:
            cards.append(suit + str(value))

    return cards


def shuffle(cards):
    for i in range(0, len(cards)):
        # Pick a random index between the current index and the end of the list
        other_position = randrange(i, len(cards))

        # Swap the current card with the one at the random position
        temp = cards[i]
        cards[i] = cards[other_position]
        cards[other_position] = temp


def main():
    cards = create_deck()
    print(f"The original dek of cards is:\n{cards}")
    print()

    shuffle(cards)
    print(f"The original dek of cards is:\n{cards}")


if __name__ == '__main__':
    main()
