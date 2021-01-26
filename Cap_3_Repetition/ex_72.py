# EXERCISE 72 : Fizz-Buzz
# Fizz-Buzz game - if the number is divisible of 3 >> Fizz, if divisible of 5 >> Buzz, both >> Fizz-Buzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZ-BUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
