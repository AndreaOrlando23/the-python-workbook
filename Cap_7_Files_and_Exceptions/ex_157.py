# EXERCISE 157 : Both letter grades and grade points

glossary = {
    "A": "4.0",
    "A-": "3.7",
    "B+": "3.3",
    "B": "3.0",
    "B-": "2.7",
    "C+": "2.3",
    "C": "2.0",
    "C-": "1.7",
    "D+": "1.3",
    "D": "1.0",
    "F": "0"
}


while True:
    user_input = input("Enter the letter grades or the grade points: ").upper()
    if user_input.strip() == "":
        break

    try:
        if user_input in glossary.keys():
            print(glossary[user_input])

        elif user_input in glossary.values():
            for key, value in glossary.items():
                if user_input == value:
                    print(key)
        else:
            print("Enter a valid letter grades or the grade points")

    except ValueError:
        print("The value entered is not valid")


"""
# Solution with def

user_input = input("Enter the letter grades or the grade points: ").upper()


def find_corresponds(grade):

    if grade in glossary.keys():
        return glossary[grade]

    elif grade in glossary.values():
        for key, value in glossary.items():
            if grade == value:
                return key


print(find_corresponds(user_input))
"""