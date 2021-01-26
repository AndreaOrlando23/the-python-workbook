# EXERCISE 61 : Is a license plate valid

plate = input("Enter the license plate: ")

if len(plate) == 6 and \
        "A" <= plate[0] <= "Z" and \
        "A" <= plate[1] <= "Z" and \
        "A" <= plate[2] <= "Z" and \
        "0" <= plate[3] <= "9" and \
        "0" <= plate[4] <= "9" and \
        "0" <= plate[5] <= "9":
    print(f"The plate {plate} is a valid older style plate.")
elif len(plate) == 7 and \
        "0" <= plate[0] <= "9" and \
        "0" <= plate[1] <= "9" and \
        "0" <= plate[2] <= "9" and \
        "0" <= plate[3] <= "9" and \
        "A" <= plate[4] <= "Z" and \
        "A" <= plate[5] <= "Z" and \
        "A" <= plate[6] <= "Z":
    print(f"The plate {plate} is a valid newer style plate.")
else:
    print(f"The plate {plate} is not valid.")
