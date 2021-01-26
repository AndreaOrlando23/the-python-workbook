# Only the Words
punctuation = [",", ".", "?", "!", "-", ":", ";"]


def contractions(s):
    without_punctuation = []
    s = s.split()
    for word in s:
        if word not in punctuation:
            without_punctuation.append(word)

    return without_punctuation


def main():
    line = input("Enter a sentence: ")
    print(f"Without punctuations: {contractions(line)}")


if __name__ == '__main__':
    main()
