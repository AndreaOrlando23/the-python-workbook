# EXERCISE 43 : Frequency to note - saw the solution
# TODO

C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88
LIMIT = 1

freq = float(input("Enter the frequency (Hz): "))

# Determine the note that corresponds to the entered frequency
# Set note equal to empty string if there isn't a match
if C4_FREQ - LIMIT <= freq <= C4_FREQ + LIMIT:
    note = "C4"
elif D4_FREQ - LIMIT <= freq <= D4_FREQ + LIMIT:
    note = "D4"
elif E4_FREQ - LIMIT <= freq <= E4_FREQ + LIMIT:
    note = "E4"
elif F4_FREQ - LIMIT <= freq <= F4_FREQ + LIMIT:
    note = "F4"
elif G4_FREQ - LIMIT <= freq <= G4_FREQ + LIMIT:
    note = "G4"
elif A4_FREQ - LIMIT <= freq <= A4_FREQ + LIMIT:
    note = "A4"
elif B4_FREQ - LIMIT <= freq <= B4_FREQ + LIMIT:
    note = "B4"
else:
    note = ""

# Display the result or an appropriate error message
if note == "":
    print("There is no note that corresponds to that frequency")
else:
    print("The frequency is", note)
