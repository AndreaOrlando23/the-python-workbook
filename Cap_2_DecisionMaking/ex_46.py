# EXERCISE 46 : What color is that square (chess)

position = input("Enter a chess board position (e.g A1): ")

col = position[0].upper()
row = int(position[1])

if col in "ACEG":
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
    print(f"The square position {position} is white")
else:
    print(f"The square position {position} is black")
