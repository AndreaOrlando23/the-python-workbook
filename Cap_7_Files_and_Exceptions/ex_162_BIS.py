# EXERCISE 162 : A book with no E BIS
from pathlib import Path

F_NAME = Path('file/In-to-the-frozen-south.txt')
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

counts = dict()

for ch in ALPHABET:
    counts[ch] = 0

num_words = 0
inf = open(F_NAME, "r")
for word in inf:
    word = word.upper().rstrip()

    unique = []
    for ch in word:
        if ch not in unique and "A" <= ch <= "Z":
            unique.append(ch)

    for ch in unique:
        counts[ch] += 1

    num_words += 1


inf.close()


smallest_count = min(counts.values())
for ch in sorted(counts):
    if counts[ch] == smallest_count:
        smallest_letter = ch
    percentage = counts[ch] / num_words * 100
    print(f"{ch} occurs in %.2f percent of words" % percentage)


print()
print(f"The letter that is easiest to avoid is {smallest_letter}")
