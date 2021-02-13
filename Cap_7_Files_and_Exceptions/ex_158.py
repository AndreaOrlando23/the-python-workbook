# EXERCISE 158 : Remove comments

try:
    in_name = input("Enter the name of a Python file: ")
    inf = open(in_name, "r")

except:
    print("A problem was encountered with the input file.")
    print("Quitting...")
    quit()


try:
    out_name = input("Enter the output file name: ")
    outf = open(out_name, "w")

except:
    inf.close()
    print("A problem was encountered with the input file.")
    print("Quitting...")
    quit()

try:
    for line in inf:
        pos = line.find("#")

        if pos > -1:
            line = line[0: pos]
            line = line + "\n"

        outf.write(line)

    inf.close()
    outf.close()

except:
    print("A problem was encountered with the input file.")
    print("Quitting...")

