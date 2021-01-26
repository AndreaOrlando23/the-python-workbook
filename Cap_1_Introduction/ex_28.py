# EXERCISE 28 : Body mass index

weight_pounds = float(input('Enter you weight in pounds: '))
height_inches = float(input('Enter your height in inches: '))

weight_kg = float(input('Enter you weight in Kg: '))
height_cm = float(input('Enter your height in cm: '))

# BMI first case (weight in pounds and height in inches)
BMI_1 = weight_pounds / (height_inches * height_inches) * 703

# BMI second case (weight in Kg and height in cm)
BMI_2 = weight_kg / (height_cm * height_cm)

print(BMI_1)
print(BMI_2)
