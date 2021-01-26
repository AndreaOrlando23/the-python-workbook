# EXERCISE 31 : Units of pressure

kiloPascals = float(input("Please enter a pressure in kilo-pascals: "))

PSI = kiloPascals * 0.145037738
mm_OfMercury = kiloPascals * 7.50062
atmospheres = kiloPascals / 101.3

print()
print("In Pounds Per Square Inch (PSI): {}".format(PSI))
print("In Millimetres Of Mercury (mmHg): {}".format(mm_OfMercury))
print("In Atmospheres (atm): {}".format(atmospheres))
