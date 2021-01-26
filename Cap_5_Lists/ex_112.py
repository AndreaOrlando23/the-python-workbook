# Remove Outliers

"""
The solution of the book is a bit different of mine, but I think that the
requirements requested can be accomplished by the following functions
"""


def remove_outliers(data):
    clean_data = sorted(data)

    # Remove the first and the last values from the clean_data list
    clean_data.pop()
    clean_data.pop(0)

    return clean_data


def main():
    values = []
    line = input("Enter a value (blank to quit): ")

    while line != "":
        num = float(line)
        values.append(num)
        line = input("Enter a value (blank to quit): ")

    if len(values) < 4:
        print("You didn't enter enough values")
    else:
        print(f"With the outliers removed: {remove_outliers(values)}")
        print(values)


main()