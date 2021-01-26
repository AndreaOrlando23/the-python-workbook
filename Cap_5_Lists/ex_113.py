# Avoiding Duplicates

words = []
duplicates = []

word = input("Enter the word (blank to quit): ")

while word != "":
    if word not in words:
        words.append(word)
    else:
        duplicates.append(word)

    word = input("Enter the word (blank to quit): ")


for word in words:
    print(word)

print(f"Duplicates removed: {duplicates}")