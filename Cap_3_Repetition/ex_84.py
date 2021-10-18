# EXERCISE 84 - Coin flip simulation

from random import randint


def sequence():
    result = ""
    count = 0
    while True:
        rand = randint(1, 2)
        if rand == 1:
            result += "T"
        else:
            result += "H"
        
        count += 1

        # Check if there are 3 equal adjacents chars
        for i in range(1, len(result)-1):
            if result[i-1] == result[i] == result[i+1]:
                return[result, count]
                quit()

def ten_sequence():
    count = 0
    for i in range(10):
        print(f"{sequence()[0]} ({sequence()[1]} flips)")
        count += sequence()[1]
    return f"On average, {count / 10} flips were needed"

print(ten_sequence())