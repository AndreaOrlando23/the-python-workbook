from ex_146 import create_card, display_card
from ex_147 import winning_card

from random import shuffle
import copy


def bingo(card):
    # list of all possible values on Bingo game
    valid_calls = [i for i in range(1, 76)]
    shuffle(valid_calls)

    call = 0
    daubered_card = copy.deepcopy(card)  # we use this card like when tou use the douber on real Bingo game

    while valid_calls != []:
        number = valid_calls.pop()
        call += 1
        
        for letter, values in daubered_card.items():
            if number in values:
                index = values.index(number)
                values[index] = 0  # replace the number at the given index

        
        if winning_card(daubered_card):
            display_card(daubered_card)
            print(f"You Won!! {call} calls needed. Last number called is: {number}\n")
            return call



card1 = {'B': [2, 14, 6, 7, 15], 
         'I': [16, 17, 18, 19, 20], 
         'N': [43, 44, 41, 33, 45], 
         'G': [48, 60, 53, 49, 57], 
         'O': [72, 65, 61, 67, 71]}


print(bingo(card1))

def play_1000_times(card):
    games = []
    card = create_card()
    for i in range(1000):
        call = bingo(card)
        games.append(call)
    
    highest_call = max(games)
    lowest_call = min(games)
    avg_call = sum(games) / 1000

    print('highest call: %d' % highest_call)
    print('lowest call: %d' % lowest_call)
    print('average call: %.1f' % avg_call)


def main():
    card = create_card()
    print(card)
    play_1000_times(card)


if __name__ == '__main__':
    main()
