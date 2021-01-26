# EXERCISE 65 : Temperature conversion table

for degrees_celsius in range(0, 101, 10):
    fahrenheit = (degrees_celsius * 9/5) + 32
    print("Celsius\t-->\tFahrenheit")
    print(degrees_celsius, "\t\t\t\t", fahrenheit)
