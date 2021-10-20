# EXERCISE 73 : Caesar Cipher


def caesar_cipher(message, shift):
# Process each character to construct the encrypted (or decrypted) message
    encrypted_message = ""
    for ch in message:
        if "a" <= ch <= "z":
            # Process a lowercase letter by determining its
            # position in the alphabet (0-25), computing its
            # new position, and adding it to the new message
            pos = ord(ch) - ord("a")
            pos = (pos + shift) % 26
            new_char = chr(pos + ord("a"))
            encrypted_message += new_char
        elif "A" <= ch <= "Z":
            # Process an uppercase letter by determining its
            # position in the alphabet (0-25), computing its
            # new position, and adding it to the new message
            pos = ord(ch) - ord("A")
            pos = (pos + shift) % 26
            new_char = chr(pos + ord("A"))
            encrypted_message += new_char
        else:
            # If the character is not a letter then copy it into the new message
            encrypted_message += ch
    
    return encrypted_message


def main():
    # Read the message and shift amount from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_cipher(message, shift)

    # Display the message
    print(f"The shifted message is: {encrypted_message}")


if __name__ == "__main__":
    main()


"""
Notes:
for negative number we have to understand the behavior of the modulus operator %
mod = n - (n//base) * base

e.g. case where shift value is positive integer and the operation pos = ord(ch) - ord("a") generate a positive integer
2 - (2//97) * 2 ==> is the same as ==> 2 % 97 ==> both result is 2

e.g. case where shift value is negative integer and the operation pos = ord(ch) - ord("a") generate a negative integer
-2 - (-2//97) * 1.25 ==> is the same as ==> -2 % 97 ==> both result is 95
"""