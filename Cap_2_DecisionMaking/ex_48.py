# EXERCISE 48 : Birth date to astrological sign

month = input("Enter the month of your birthday: ").lower()
day = int(input("Enter the day of your birthday: "))
sign = ""

assert day <= 31

if (month == "january" and day >= 20) or (month == "february" and day <= 18):
    sign = "Aquarius"
elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
    sign = "Pisces"
elif (month == "march" and day >= 21) or (month == "april" and day <= 19):
    sign = "Aries"
elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    sign = "Taurus"
elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
    sign = "Gemini"
elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
    sign = "Cancer"
elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
    sign = "Leo"
elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
    sign = "Virgo"
elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
    sign = "Libra"
elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
    sign = "Scorpio"
elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
    sign = "Aries"
elif (month == "december" and day >= 22) or (month == "january" and day <= 21):
    sign = "Capricorn"

print("You're sign is:", sign)
