# EXERCISE 33 : Sort 3 integers

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

smallest = min(number1, number2, number3)
largest = max(number1, number2, number3)
middle = (number1 + number2 + number3) - smallest - largest

print('The sorted order of your numbers is:', smallest, middle, largest)
