# Reverse Order

# Stores integers entered by the user in line input
data = []
line = int(input("Enter an integer (0 to quit): "))

while line != 0:
    data.append(line)
    line = int(input("Enter an integer (0 to quit): "))

# Rearranges the value in data in reverse order
data.sort(reverse=True)

# Display the integers in data on each line
for i in data:
    print(i)