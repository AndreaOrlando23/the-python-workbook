# Sorted Order

# Stores integers entered by the user in line input
data = []
line = int(input("Enter an integer (0 to quit): "))

while line != 0:
    data.append(line)
    line = int(input("Enter an integer (0 to quit): "))

data.sort()

# Display the integers in data (in ascending order) on each line
for i in data:
    print(i)
