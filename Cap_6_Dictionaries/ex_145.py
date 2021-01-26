# EXERCISE 145 : Scrabble Score

points_letters = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
                  2: ['D', 'G'],
                  3: ['B', 'C', 'M', 'P'],
                  4: ['F', 'H', 'V', 'W', 'Y'],
                  5: ['K'],
                  8: ['J', 'X'],
                  10: ['Q', 'Z']}


score = []
word = input("Enter your word: ").upper()

for char in word:
    for point, letter in points_letters.items():
        if char in points_letters[point]:
            score.append(point)


print(score)
result = sum(score)

print(f"{word} is worth {result}")

