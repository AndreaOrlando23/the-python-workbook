# EXERCISE 160 : Weird words

from string import punctuation

ie_list = []
cei_list = []
# weird words
ei_list = []
cie_list = []

text = input("Enter the file name: ")

with open(text, "r") as file:
    line = file.read()
    line = line.translate(str.maketrans("", "", punctuation)).lower()
    words = line.split()

    for i in range(len(words)):

        if "cie" in words[i]:
            if words[i] not in cie_list:
                cie_list.append(words[i])

        if "ie" in words[i]:
            if words[i] not in ie_list:
                ie_list.append(words[i])

        if "cei" in words[i]:
            if words[i] not in cei_list:
                cei_list.append(words[i])

        if "ie" in words[i]:
            if words[i] not in ie_list:
                ie_list.append(words[i])


print()
print("The following lists follow the rule 'I before E except after C':")
print(f"Words with 'ie': {ie_list}")
print(f"Words with 'cei': {cei_list}")
print('-' * 200)
print("The following lists do not follow the rule:")
print(f"Words with 'cie: {cie_list}")
print(f"Words with 'ei': {ei_list}")


