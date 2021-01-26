# EXERCISE 173 : Total the Values


def total_values():
    values = input("Enter a number (blank to quit): ")
    if values == "":
        return 0.0

    else:
        num = float(values)
        total = num + total_values()
        return total


result = total_values()
print(result)
