# EXERCISE 73 : Caesar Cipher with OOP

class CaesarCipher:

    def __init__(self, message, shift=0):
        self.message = message
        self.shift = shift
    
    
    def get_message(self):
        return f"{self.message}"

    
    def encrypted_message(self):
        new_message = ""
        for ch in self.message:
            if "a" <= ch <= "z":
                # Process a lowercase letter by determining its
                # position in the alphabet (0-25), computing its
                # new position, and adding it to the new message
                pos = ord(ch) - ord("a")
                pos = (pos + self.shift) % 26
                new_char = chr(pos + ord("a"))
                new_message += new_char
            elif "A" <= ch <= "Z":
                # Process an uppercase letter by determining its
                # position in the alphabet (0-25), computing its
                # new position, and adding it to the new message
                pos = ord(ch) - ord("A")
                pos = (pos + self.shift) % 26
                new_char = chr(pos + ord("A"))
                new_message += new_char
            else:
                # If the character is not a letter then copy it into the new message
                new_message += ch
    
        return new_message


class Ticket(CaesarCipher):
    
    def print_ticket(self):
        table_line = '+'+'='*70+'+'
        title= '|{:^70}|'.format('Caesar Cipher Algo')
        original_message = '|{:^70}|'.format('Original message: '+ self.get_message())
        encrypted_message = '|{:^70}|'.format('Encrypted message: '+ self.encrypted_message())
        decorator = '{:^70}'.format('~')
    
        return f"""
        {decorator}
        {table_line}
        {title}
        {table_line}
        {original_message}
        {encrypted_message}
        {table_line}
        {decorator}
        """


def main():

    # Read the message and shift amount from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    ticket = Ticket(message, shift)
    result = ticket.print_ticket()

    print(result)


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