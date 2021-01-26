# EXERCISE 55 : Wavelengths of visible light

wavelength = int(input("Enter the wavelength: "))
color = ""

if 380 <= wavelength < 450:
    color = "Violet"
elif 450 <= wavelength < 495:
    color = "Blue"
elif 495 <= wavelength < 570:
    color = "Green"
elif 570 <= wavelength < 590:
    color = "Yellow"
elif 590 <= wavelength < 620:
    color = "Orange"
elif 620 <= wavelength <= 750:
    color = "Red"

if wavelength < 380 or wavelength > 750:
    print(f"ERROR: the wavelength {wavelength} is outside of the visible spectrum")
else:
    print(f"The color of wavelength {wavelength} is {color}")
