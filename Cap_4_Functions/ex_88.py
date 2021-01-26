# EXERCISE 88 : Median of three values - SOLUTION 1


def median_of_values(a, b, c):
    values = [a, b, c]
    sorted_values = sorted(values)
    return sorted_values[1]


def main():
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = int(input("Enter the third value: "))

    if x == "" or y == "" or z == "":
        print("ERROR: enter 3 values")
        quit()

    median = median_of_values(x, y, z)
    print(f"The median of these values is: {median}")


main()
