# EXERCISE 152 : Number the lines in a file

fname = input("Enter the file name: ")
new_file = input("Enter the name of the new file: ")

inf1 = open(fname, "r")
inf2 = open(new_file, "w")

index = 1
for word in inf1:
    inf2.write(f"{index}: {word}")
    index += 1

inf1.close()
inf2.close()

output = open(new_file, "r")

for word in output:
    line = word.strip()
    print(line)

output.close()