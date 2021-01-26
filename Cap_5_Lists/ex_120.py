# Formatting a list


def format_list(items):

    if len(items) == 0:
        return "<empty list>"
    if len(items) == 1:
        return str(items[0])

    list_of_items = ""

    for i in range(0, len(items) - 2):
        list_of_items += str(items[i]) + ", "

    list_of_items += str(items[len(items) - 2]) + " and "
    list_of_items += str(items[len(items) - 1])

    return list_of_items


def main():

    items = []
    line = input("Enter an Item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an Item (blank to quit): ")

    print(format_list(items))


main()
