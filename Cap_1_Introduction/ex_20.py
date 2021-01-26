# EXERCISE 20 : Ideal Gas Law

P = float(input('Enter the value of the pressure in Pascals: '))
V = float(input('Enter the value of the volume in liters: '))
T = float(input('Enter the value of the temperature in Kelvin: '))

R = 8314

# Compute the Ideal Gas Law
IGL = (P*V) / (R*T)

print("The amount of gas in moles for these conditions is {}.".format(IGL))
