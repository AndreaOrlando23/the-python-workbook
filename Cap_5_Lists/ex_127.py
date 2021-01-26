# EXERCISE 127 : Is a List already in Sorted Order?


def is_sorted(values):

    if len(values) == 0:
        print("The list is empty")
        quit()
    elif len(values) == 1:
        print("There is only one element in the list")
        quit()

    if values == sorted(values) or values == sorted(values, reverse=True):
        return True
    else:
        return False


def main():

    list_of_values = []
    v = input("Enter a value (blank to quit): ")

    while v != "":
        values = int(v)
        list_of_values.append(values)
        v = input("Enter a value (blank to quit): ")

    if is_sorted(list_of_values):
        print("The list is in sorted order")
    else:
        print("The list is not in sorted order")


main()