def deck(self):
    self.cards = []
    for suit in range(4):
        for rank in range(1, 14):
            card = Card(suit, rank)
            self.cards.append(card)