# EXERCISE 56 : Frequency to name

frequency = float(input("Enter a frequency: "))
category = ""

if frequency < 3e9:
    category = "radio waves"
elif 3e9 <= frequency < 3e12:
    category = "microwaves"
elif 3e12 <= frequency < 4.3e14:
    category = "infrared light"
elif 4.3e14 <= frequency < 7.5e14:
    category = "visible light"
elif 7.5e14 <= frequency < 3e17:
    category = "ultraviolet light"
elif 3e17 <= frequency < 3e19:
    category = "x-rays"
elif frequency >= 3e19:
    category = "gamma rays"

if category != "":
    print("This frequency is in the '{}' category.".format(category))
else:
    print("Invalid frequency entered")
