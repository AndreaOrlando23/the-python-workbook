# EXERCISE 68 : Compute a grade point average - SOLUTION 1

# Store the grades
total_grades = 0
total_letters = 0

letter_grades = input("Enter the letter grade: ").upper()

while letter_grades != "":

    if letter_grades == "A+" or letter_grades == "A":
        grade_points = 4.0
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "A-":
        grade_points = 3.7
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "B+":
        grade_points = 3.3
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "B":
        grade_points = 3.0
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "B-":
        grade_points = 2.7
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "C+":
        grade_points = 2.3
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "C":
        grade_points = 2.0
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "C-":
        grade_points = 1.7
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "D+":
        grade_points = 1.3
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "D":
        grade_points = 1.0
        total_grades += grade_points
        total_letters += 1

    elif letter_grades == "F":
        grade_points = 0
        total_grades += grade_points
        total_letters += 1

    letter_grades = input("Enter the letter grade: ").upper()

avg = total_grades / total_letters

print(f"The average grade point is: {avg}")
