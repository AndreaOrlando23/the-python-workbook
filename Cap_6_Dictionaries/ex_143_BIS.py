# EXERCISE 143 : Anagrams BIS


def character_counts(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


def main():
    s1 = input("Enter the first string: ").replace(" ", "")
    s2 = input("Enter the second string: ").replace(" ", "")

    counts_1 = character_counts(s1)
    counts_2 = character_counts(s2)

    print(counts_1)
    print(counts_2)

    if counts_1 == counts_2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")


main()
