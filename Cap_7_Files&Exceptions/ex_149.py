# EXERCISE 149 : Display the head of a file

file_name = input("Enter the name of a file and see the first 10 lines: ")

file_opened = False
while not file_opened:
    try:
        inf = open(file_name)
        file_opened = True
    except FileNotFoundError:
        print(f"{file_name} was not found, please try again")
        file_name = input("Enter the name of the file: ")


index = 0
for position, word in enumerate(inf):
    line = word.strip()
    print(position + 1, line)
    index += 1
    if index >= 10:
        break

inf.close()


