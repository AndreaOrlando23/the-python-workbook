# EXERCISE 90 : The twelve days of Christmas


def int_to_ordinal(i):
    if i < 1 or i > 12:
        print("No gifts")

    return i


def display_verse(n):
    print(f"Oh the {int_to_ordinal(n)} day of Christmas")
    print("my true love sent to me:")

    if n == 12:
        print("Twelve drummers drumming,")
    if n == 11:
        print("Eleven pipers piping,")
    if n == 10:
        print("The lords a-leaping,")
    if n == 9:
        print("Nine ladies dancing,")
    if n == 8:
        print("Eight maids a-milking,")
    if n == 7:
        print("Seven swans a-swimming,")
    if n == 6:
        print("Six geese a-laying,")
    if n == 5:
        print("Five golden rings,")
    if n == 4:
        print("Four golden rings,")
    if n == 3:
        print("Three French hens,")
    if n == 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()


def main():
    for verse in range(1, 13):
        display_verse(verse)


main()
