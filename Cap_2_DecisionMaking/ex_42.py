# EXERCISE 42 : Note to frequency

# Store the fourh octave values
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

note = input("Enter the two character note name, such as C4: ").replace(" ","").upper()

# Store the note and its frequency in separate variables
char = note[0]
freq = int(note[1])

# Get frequency of the note, assuming it is in the fourth octave
if char == "C":
    fourth_octave = C4
elif note == "D":
    fourth_octave = D4
elif note == "E":
    fourth_octave = E4
elif note == "F":
    fourth_octave = F4
elif note == "G":
    fourth_octave = G4
elif note == "A":
    fourth_octave = A4
elif note == "B":
    fourth_octave = B4

# Now adjust the frequency to bring it into the correct octave
result = fourth_octave / 2 ** (4 - freq)

# Display the result
print(f"The frequency of {note} is {result}")
