# EXERCISE 183 : Element Sequences

elements = []
file = open('elements.txt')
lines = file.readlines()

for el in lines:
    element = el.split(',')[2].strip()
    elements.append(element)

elements.sort()
print(elements)


def domino_elements(word, elements_list):
    if word == "":
        return []

    result = []
    last_char = word[len(word)-1].lower()

    for i in range(0, len(elements_list)):
        first_char = elements_list[i][0].lower()

        if first_char == last_char:
            candidate = domino_elements(elements_list[i], elements_list[0:i] + elements_list[i+1:len(elements_list)])

            if len(candidate) > len(result):
                result = candidate

    return [word] + result


def main():
    word = input("Enter a chemical element: ").capitalize()

    if word in elements:
        result = domino_elements(word, elements)
        print(f"Your best sequence with {word} is:")

        for index, word in enumerate(result):
            print(index+1, word)

    else:
        print(f"Your word '{word}' is not a valid chemical element")


main()