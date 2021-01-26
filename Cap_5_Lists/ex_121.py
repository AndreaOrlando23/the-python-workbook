# Random Lottery Numbers
from random import randrange

MIN = 1
MAX = 49
NUM = 6

ticket = []

for i in range(NUM):
    rand = randrange(MIN, MAX + 1)
    while rand in ticket:
        rand = randrange(MIN, MAX + 1)

    ticket.append(rand)

print("Your numbers in ticket are: ", end="")
for n in sorted(ticket):
    print(n, end=" ")
print()


"""
The following function could achieved the same output
but you have to import all the random module
random.sample(range(MIN, MAX+1), NUM)
"""