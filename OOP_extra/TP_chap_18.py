from random import random, shuffle


"""
Suits:
Spades --> 3
Hearts --> 2
Diamonds --> 1
Clubs --> 0

Ranks faces:
Jack --> 11
Queen --> 12
King --> 13
each of the numerical ranks maps to the corresponding integer
"""


class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # First rank is None because there are no cards with rank 0
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check ranks
        return self.rank < other.rank

    """
    more concisely version of def __lt__() with tuple comparison
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    """


# card1 = Card(2, 11)
# print(card1)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()


deck = Deck()
print(deck)


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


hand = Hand('new hand')
print(hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)