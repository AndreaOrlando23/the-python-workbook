# EXERCISE 17 : Heat capacity

# Define the constant for the specific heat capacity of water and the price  of electricity
WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

volume = float(input('Amount of water in millimeters: '))
d_temp = float(input('Temperature increase (degrees Celsius): '))

# Compute the energy in Joules
q = volume * d_temp * WATER_HEAT_CAPACITY

print('That will require %d Joules of energy.' % q)

# Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

# Display the cost
print('That much energy will cost %.2f cents.' % cost)
