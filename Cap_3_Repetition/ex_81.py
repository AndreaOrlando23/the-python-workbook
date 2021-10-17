# EXERCISE 81 : Binary to Decimal

num = input("Enter a valid binary (base 2) number: ")

for n in num:
    if n > "1" or n < "0":
        print(" Please enter a valid binary (base 2) number.")
        num = input("Enter a valid binary (base 2) number: ")

invert_num = num[::-1]  # if num = 100, then invert_num = 001

index = 0
result = 0
while index <= len(invert_num) - 1:
    conversion = int(invert_num[index]) * (2 ** index)
    index += 1
    result += conversion

print(f"The conversion of binary {invert_num} in decimal is: {result}")
