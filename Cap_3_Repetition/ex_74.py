# EXERCISE 74 : Square root

x = float(input("Enter a number: "))
guess = x/2
epsilon = 0.0000001

while guess >= epsilon:
    guess = guess/2
    print(guess)
