# EXERCISE 84 - Coin flip simulation
# TODO

from random import randint

tails_count = 0
heads_count = 0

for i in range(10):
    rand = randint(1, 2)
    if rand == 1:
        tails_count += 1
        print("T", end=" ")
    else:
        heads_count += 1
        print("H", end=" ")
