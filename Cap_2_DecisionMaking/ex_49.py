# EXERCISE 49 : Chinese Zodiac

year = int(input('Enter the year: '))
zodiac = ""

if year >= 0:
    if year % 12 == 8:
        zodiac = "Dragon"
    elif year % 12 == 9:
        zodiac = "Snake"
    elif year % 12 == 10:
        zodiac = "Horse"
    elif year % 12 == 11:
        zodiac = "Sheep"
    elif year % 12 == 0:
        zodiac = "Monkey"
    elif year % 12 == 1:
        zodiac = "Rooster"
    elif year % 12 == 2:
        zodiac = "Dog"
    elif year % 12 == 3:
        zodiac = "Pig"
    elif year % 12 == 4:
        zodiac = "Rat"
    elif year % 12 == 5:
        zodiac = "Ox"
    elif year % 12 == 6:
        zodiac = "Tiger"
    elif year % 12 == 7:
        zodiac = "Hare"
else:
    zodiac = "Enter a integer positive number"

print("%d is the year of the %s" % (year, zodiac))
