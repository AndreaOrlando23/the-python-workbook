# EXERCISE 4 : Area of a field

SQFT_PER_ACRE = 43.560  # square feet per acre

width = float(input("Enter the width of the farmer's field in feet: "))
length = float(input("Enter the length of the farmer's field in feet: "))
acres = width * length / SQFT_PER_ACRE

print("The area of the field is %.2f acres" % acres)
