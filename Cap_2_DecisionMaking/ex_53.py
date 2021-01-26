# EXERCISE 53 : Grade points

A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
INVALID = -1

grade_points = float(input("Enter your grade points: "))
letter = ""

if grade_points > A:
    letter = "A+"
elif grade_points == A:
    letter = "A"
elif A > grade_points >= A_MINUS:
    letter = "A-"
elif A_MINUS > grade_points >= B_PLUS:
    letter = "B+"
elif B_PLUS > grade_points >= B:
    letter = "B"
elif B > grade_points >= B_MINUS:
    letter = "B-"
elif B_MINUS > grade_points >= C_PLUS:
    letter = "C+"
elif C_PLUS > grade_points >= C:
    letter = "C"
elif C > grade_points >= C_MINUS:
    letter = "C-"
elif C_MINUS > grade_points >= D_PLUS:
    letter = "D+"
elif D_PLUS > grade_points >= D:
    letter = "D"
elif D > grade_points >= F:
    letter = "F"
else:
    letter = INVALID

if letter == INVALID:
    print("Please enter a correct value")
else:
    print(f"Your grade points {grade_points} is equal to {letter}")
