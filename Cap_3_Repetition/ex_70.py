# EXERCISE 70 : Parity Bits

line = input("Enter 8 bits (blank to exit): ")

while line != "":
    # Ensure that the line has a total of 8 zeros and ones and exactly 8 characters
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        print("That wasn't 8 bits... Try again.")
    else:
        # Count the number of ones
        ones = line.count("1")

        # Display the parity bit
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")

    # Read the next line of input
    line = input("Enter 8 bits: ")
