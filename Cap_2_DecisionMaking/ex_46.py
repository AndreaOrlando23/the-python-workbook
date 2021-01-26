# EXERCISE 46 : What color is that square (chess)

position = input("Enter a chess board position: ")

col = position[0].lower()
row = int(position[1])

if col in "aceg":
    starts_with_black = True
else:
    starts_with_black = False


if starts_with_black:
    if row % 2 == 0:
        white = True
    else:
        white = False
else:
    if row % 2 == 0:
        white = False
    else:
        white = True

if white:
    print(f"The position {position} is colored white")
else:
    print(f"The position {position} is colored black")
