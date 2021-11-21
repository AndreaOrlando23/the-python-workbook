from ex_146 import create_card, display_card
from ex_147 import winning_card

from random import shuffle
import copy


def bingo(card):
    # list of all possible values on Bingo game
    valid_calls = [i for i in range(1, 76)]
    shuffle(valid_calls)

    calls = 0
    '''
    We'll use daubered_card to replace nums extracted with value 0 
    It will helpfull for the logic of winning_card() function
    The name daubered is ispired by the dauber use in Bingo game
    '''
    daubered_card = copy.deepcopy(card)

    while valid_calls != []:
        number = valid_calls.pop()
        calls += 1
        
        for letter, values in daubered_card.items():
            if number in values:
                index = values.index(number)
                values[index] = 0  # replace the number with 0 at the given index

        
        if winning_card(daubered_card):
            display_card(daubered_card)
            print(f"You Won!! {calls} calls needed. Last number called is: {number}\n")
            return calls


def play_1000_times(card):
    games = []
    card = create_card()
    for i in range(1000):
        calls = bingo(card)
        games.append(calls)
    
    highest_calls = max(games)
    lowest_calls = min(games)
    avg_calls = sum(games) / len(games)  # -> 1000

    print('Highest calls: %d' % highest_calls)
    print('Lowest calls: %d' % lowest_calls)
    print('Average calls: %.1f' % avg_calls)


def main():
    card = create_card()
    print(card)
    play_1000_times(card)


if __name__ == '__main__':
    main()
