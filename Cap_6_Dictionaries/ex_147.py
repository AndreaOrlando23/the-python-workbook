# Checking for a winning card (Bingo)
from ex_146 import display_card


def vertical_check(card):
    for letter in card:
        if sum(card[letter]) == 0:
            return True
    return False


def horizontal_check(card):
    sum_values = 0
    for i in range(5):
        for letter in card:
            sum_values += card[letter][i]
        if sum_values == 0:
            return True

        sum_values = 0  # reset my_sum variable

    return False
    

def diagonal_check(card):
    sum_values = 0
    i = 0
    for letter in card:
        sum_values += card[letter][i]
        i += 1  # iterate to keys in diagonal from left to right
    
    if sum_values == 0:
        return True
    
    sum_values = 0
    i = 4
    for letter in card:
        sum_values += card[letter][i]
        i -= 1  # iterate to keys in diagonal from right to left
    
    if sum_values == 0:
        return True
    
    return False


def winning_card(card):
    if vertical_check(card) or horizontal_check(card) or diagonal_check(card):
        return True
    return False


def main():
    # vertical check
    card1 = {'B': [2, 14, 6, 7, 15], 
             'I': [0, 0, 0, 0, 0], 
             'N': [43, 44, 41, 33, 45], 
             'G': [48, 60, 53, 49, 57], 
             'O': [72, 65, 61, 67, 71]}

    # horizontal check
    card2 = {'B': [2, 14, 0, 7, 15],
             'I': [23, 20, 0, 22, 21],
             'N': [43, 44, 0, 33, 45], 
             'G': [48, 60, 0, 49, 57], 
             'O': [72, 65, 0, 67, 71]}
             
    # diagonal check (from left to right)
    card3 = {'B': [0, 14, 6, 7, 15],
             'I': [23, 0, 24, 22, 21],
             'N': [43, 44, 0, 33, 45], 
             'G': [48, 60, 53, 0, 57], 
             'O': [72, 65, 61, 67, 0]}

    # diagonal check (from right to left)
    card4 = {'B': [2, 14, 6, 7, 0], 
             'I': [23, 20, 24, 0, 21],
             'N': [43, 44, 0, 33, 45],
             'G': [48, 0, 53, 49, 57],
             'O': [0, 65, 61, 67, 71]}

    # bad card
    bad_card = {'B': [2, 0, 0, 0, 0],
                'I': [0, 20, 0, 0, 0],
                'N': [0, 0, 0, 33, 0],
                'G': [0, 0, 53, 0, 0],
                'O': [72, 0, 0, 0, 71]}
    

    display_card(card1)
    print(winning_card(card1))

    display_card(card2)
    print(winning_card(card2))

    display_card(card3)
    print(winning_card(card3))

    display_card(card4)
    print(winning_card(card4))

    display_card(bad_card)
    print(winning_card(bad_card))



if __name__ == '__main__':
    main()
