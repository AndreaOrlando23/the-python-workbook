# EXERCISE 94 : Is it a valid triangle?


def valid_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        return False
    return True


def main():
    length1 = int(input("Enter the first length: "))
    length2 = int(input("Enter the second length: "))
    length3 = int(input("Enter the third length: "))

    if valid_triangle(length1, length2, length3):
        print("Yes! It is a valid triangle")
    else:
        print("Nope! It is not a valid triangle")


main()
