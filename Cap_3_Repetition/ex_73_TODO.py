# EXERCISE 73 : Caesar Cipher

# Read the message and shift amount from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Process each character to construct the encrypted (or decrypted) message
new_message = ""
for ch in message:
    if "a" <= ch <= "z":
        # Process a lowercase letter by determining its
        # position in the alphabet (0-25), computing its
        # new position, and adding it to the new message
        pos = ord(ch) - ord("a")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("a"))
        new_message += new_char
    elif "A" <= ch <= "Z":
        # Process an uppercase letter by determining its
        # position in the alphabet (0-25), computing its
        # new position, and adding it to the new message
        pos = ord(ch) - ord("A")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_message += new_char
    else:
        # If the character is not a letter then copy it into the new message
        new_message += ch

# Display the message
print(f"The shifted message is: {new_message}")
