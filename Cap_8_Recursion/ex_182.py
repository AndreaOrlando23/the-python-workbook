# EXERCISE 182 : Spelling with element symbols

elements = open('elements.txt')
all_lines = elements.readlines()

# Create a dictionary of element as {symbol: element}
dict_of_elem = {}
for el in all_lines:
    if el not in dict_of_elem:
        dict_of_elem.update({
            el.split(',')[1]: el.split(',')[2].strip()
        })


# print(dict_of_elem)

def spelling_with_symbols(word, elements_dict, i=0, result=""):
    if word[i].capitalize() in elements_dict:
        result += word[i].capitalize()
        i += 1

        if i == len(word):
            return result
        else:
            return spelling_with_symbols(word, elements_dict, i, result)

    if i < len(word) - 1:
        if word[i].capitalize() + word[i + 1] in elements_dict:
            result += word[i].capitalize() + word[i + 1]
            i += 2

            if i == len(word):
                return result
            else:
                return spelling_with_symbols(word, elements_dict, i, result)

    else:
        return False


def main():
    word = input("Enter a word: ")
    result = spelling_with_symbols(word, dict_of_elem)

    if result:
        print(f"{word} can be spelled as {result}")
    else:
        print(f"Your word '{word}' can't be spelled as using element symbols")

    # TODO
    """
    for symbol, elem in dict_of_elem.items():
        if spelling_with_symbols(dict_of_elem[elem], dict_of_elem):
            print(f"{elem} can be spelled as:")
    """


main()