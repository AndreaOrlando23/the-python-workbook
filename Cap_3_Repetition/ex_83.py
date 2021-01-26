# EXERCISE 83 : Maximum integer - SOLUTION 1
from random import randrange

integer = randrange(1, 101)
print(integer)

print('-'*50)

for i in range(randrange(1, 101)):
    current = randrange(1, 101)
    if current > integer:
        integer = current
        print(f"{current} --> Update")
    else:
        print(current)
