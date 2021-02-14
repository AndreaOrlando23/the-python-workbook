# EXERCISE 169 : Redacting text in a file

inf_name = input("Enter the name of the text file to redact: ")
inf = open(inf_name, "r")

# Get the name of the sensitive words file and open it
sen_name = input("Enter the name of the sensitive words file: ")
sen = open(sen_name, "r")

# Load the sensitive words into a list
words = list()
line = sen.readline()
while line != "":
    line = line.rstrip()
    words.append(line)

    line = sen.readline()

# The sensitive word file can be closed at this point because all of the words have been read into a list
sen.close()

# Get the name of the output file and open it
outf_name = input("Enter the name for the new redacted file: ")
outf = open(outf_name, "w")

# Read each line from the input file. Replace all of the sensitive words with asterisks.
line = inf.readline()
while line != "":
    for word in words:
        line = line.replace(word, "*" * len(word))

    outf.write(line)

    line = inf.readline()

inf.close()
outf.close()
