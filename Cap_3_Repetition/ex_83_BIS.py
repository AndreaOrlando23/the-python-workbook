# EXERCISE 83 : Maximum integer - SOLUTION 2
from random import randrange

NUM_ITEMS = 100

# Generate the first number and display it
mx_value = randrange(1, NUM_ITEMS + 1)
print(mx_value)

# Count the number of times the maximum value is updated
num_updates = 0

# For each of the remaining numbers
for i in range(1, NUM_ITEMS + 1):
    # Generate a new random number
    current = randrange(1, NUM_ITEMS + 1)

    if current > mx_value:
        # Update the maximum and count the update
        mx_value = current
        num_updates += 1

        print(f"{current} <== Update")

    else:
        print(current)


print(f"The maximum value found was {mx_value}")
print(f"The maximum value was updated {num_updates} times")
