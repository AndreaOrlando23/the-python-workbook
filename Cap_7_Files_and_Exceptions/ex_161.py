# EXERCISE 161 : What's that element again?

while True:
    user_input = input("Enter the number of protons or name or symbol element: ").lower()
    if user_input == "":
        break

    try:
        with open("elements.txt", "r") as file:
            protons = dict()
            symbols = dict()
            elements = dict()
            for line in file:
                line = line.replace("\n", "").lower()
                line = line.split(",")

                protons[line[0]] = (line[1], line[2])
                symbols[line[1]] = (line[0], line[2])
                elements[line[2]] = (line[0], line[1])

            if user_input in protons:
                print(user_input, protons[user_input])

            if user_input in symbols:
                print(user_input, symbols[user_input])

            if user_input in elements:
                print(user_input, elements[user_input])

    except ValueError:
        print("The input is not valid.")

