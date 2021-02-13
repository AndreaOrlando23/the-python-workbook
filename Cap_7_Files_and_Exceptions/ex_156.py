# EXERCISE 156 : Sum a collection of numbers
import re

n = input("Enter a number: ")
# num = isinstance(n, float)
sum_nums = 0

while n != "":
    try:
        num = float(n)
        sum_nums += num
        print(sum_nums)

    except ValueError:
        print("Non-numeric data found in input")

    n = input("Enter a number: ")

print(f"The total is: {sum_nums}")