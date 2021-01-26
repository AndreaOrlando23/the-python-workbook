# EXERCISE 136 : Reverse Lookup


def reverse_lookup(d, v):
    list_of_key = []
    for key in d:
        if d[key] == v:
            list_of_key.append(key)
    return list_of_key


def main():
    it_en = {"il": "the", "la": "the", "libro": "book", "cane": "dog"}

    print(f"The italian word for 'the' are: {reverse_lookup(it_en, 'the')}")
    print("Expected: ['il', 'la']")
    print()

    print(f"The italian word for 'dog' are: {reverse_lookup(it_en, 'dog')}")
    print("Expected: ['cane']")
    print()

    print(f"The italian word for 'adaadfj' are: {reverse_lookup(it_en, 'akdjbkfba')}")
    print("Expected: []")
    print()


if __name__ == '__main__':
    main()