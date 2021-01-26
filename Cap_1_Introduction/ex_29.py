# EXERCISE 29 : Wind Chill


def wind_chill():
    degree = float(input('Enter the air temperature (degrees Celsius): '))
    wind = float(input('Enter the wind speed (kilometers per hour): '))
    WCI = (13.12 + 0.6215 * degree) - (11.37 * wind ** 0.16 + 0.3965 * degree * wind ** 0.16)

    if degree >= 10 and wind > 4.8:
        return round(WCI)  # Display the result rounded to the closest integer
    else:
        print('The air temperature must be less or equal then 10 degrees Celsius and the wind speed exceeding 4.8 Km/h')


print(wind_chill())
