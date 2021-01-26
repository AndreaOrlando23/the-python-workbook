# EXERCISE 32 : Sum of the digits in an integer

number = input('Enter a four-digit integer: ')

# sum_of_digits = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])  # my solution
sum_of_digits = int(number[0])
sum_of_digits += int(number[1])
sum_of_digits += int(number[2])
sum_of_digits += int(number[3])

print('The sum of its digits is:', sum_of_digits)
