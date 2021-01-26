# EXERCISE 63 : Average

sum_values = 0
num_values = 0

interrupted = False
while not interrupted:
    values = int(input("Enter a collection of values (0 to exit): "))
    if values == 0:
        interrupted = True
    else:
        sum_values += values
        num_values += 1

average = sum_values / num_values

print(f"The average is {average}")
