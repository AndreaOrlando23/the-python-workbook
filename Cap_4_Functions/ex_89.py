# EXERCISE 89 : Convert an integer to its ordinal number


def ordinal_number(i):
    if i == 1:
        i = "1 - First"
    elif i == 2:
        i = "2 - Second"
    elif i == 3:
        i = "3 - Third"
    elif i == 4:
        i = "4 - Fourth"
    elif i == 5:
        i = "5 - Fifth"
    elif i == 6:
        i = "6 - Sixth"
    elif i == 7:
        i = "7 - Seventh"
    elif i == 8:
        i = "8 - Eighth"
    elif i == 9:
        i = "9 - Nineth"
    elif i == 10:
        i = "10 - Tenth"
    elif i == 11:
        i = "11 - Eleventh"
    elif i == 12:
        i = "12 - Twelfth"

    return i


def main():
    number = int(input("Enter a number from 1 to 12: "))

    if number < 1 or number > 12:
        print("ERROR")

    for i in range(number, 13):
        conversion = ordinal_number(number)
        print(conversion)
        number += 1


main()
