# EXERCISE 71 : Approximate pi - SOLUTION 1
# Ho provato a inserire un valore incrementale per calcolare l'approssimazione ma per ora non sono riuscito

a = 2
b = 3
c = 4

i = 2

first_series = c / (a * b * c)
second_series = c / ((a+i) * (b+i) * (c+i))

for i in range(1, 16):
    pi = 3
    step_one = pi + first_series - second_series
    first_series = second_series
    i += 2
    step_two = pi + first_series - second_series
