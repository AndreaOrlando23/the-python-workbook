# EXERCISE 140 : Postal Codes

first_char_provence = {'Newfounland': 'A',
                       'Nuova Scotia': 'B',
                       'Prince Edward Island': 'C',
                       'New Brunswick': 'E',
                       'Quebec': ['G', 'H', 'J'],
                       'Ontario': ['K', 'L', 'M', 'N', 'P'],
                       'Manitoba': 'R',
                       'Saskatchewan': 'S',
                       'Alberta': 'T',
                       'British Columbia': 'V',
                       'Nunavut': 'X',
                       'Northwest Territories': 'X',
                       'Yukon': 'Y'}

invalid_code = ['D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z']


def identifies_postal_code(postal_code):
    if postal_code[0] in invalid_code:
        print(f"The postal code {postal_code} is not valid")

    for key in first_char_provence:

        if first_char_provence[key] == postal_code[0] and postal_code[0] != 'X':
            if postal_code[1] == 0:
                print(f'The postal code {postal_code} is for rural address in {key}')
            else:
                print(f'The postal code {postal_code} is for urban address in {key}')

    if postal_code[0] == 'X':
        if postal_code[1] == 0:
            print(f'The postal code {postal_code} is for rural address in Nunavut or Northwest Territories')
        else:
            print(f'The postal code {postal_code} is for urban address in Nunavut or Northwest Territories')


def main():
    postal_code = input("Enter your postal code: ").upper()
    identifies_postal_code(postal_code)


main()