# EXERCISE 172 : Words with six vowels

file_name = input("Enter the file name: ")
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

with open(file_name, "r") as file:
    try:
        for lines in file:
            for word in lines:
                accumulate = []

                for ch in word:
                    if ch in VOWELS:
                        accumulate.append(ch)
                        if sorted(accumulate) == VOWELS:
                            print(f"{word} have all the vowels ordered inside")

    except IOError:
        print("Something went wrong while running the file")
        quit()
