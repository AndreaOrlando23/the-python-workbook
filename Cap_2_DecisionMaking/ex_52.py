# EXERCISE 52 : Letter grade to grade points

letter = input("Enter the letter grade: ").upper()
invalid = -1
grade_points = ""

if letter == "A+" or letter == "A":
    grade_points = 4.0
elif letter == "A-":
    grade_points = 3.7
elif letter == "B+":
    grade_points = 3.3
elif letter == "B":
    grade_points = 3.0
elif letter == "B-":
    grade_points = 2.7
elif letter == "C+":
    grade_points = 2.3
elif letter == "C":
    grade_points = 2.0
elif letter == "C-":
    grade_points = 1.7
elif letter == "D+":
    grade_points = 1.3
elif letter == "D":
    grade_points = 1.0
elif letter == "F":
    grade_points = 0
else:
    grade_points = invalid

if grade_points == invalid:
    print("That wasn't a valid letter grade")
else:
    print(f"A(n) {letter} is equal to {grade_points} grade points")
