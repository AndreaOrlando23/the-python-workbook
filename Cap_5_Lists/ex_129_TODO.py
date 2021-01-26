# EXERCISE 129 : Tokenizing a String


def token_list(s):
    symbol = ["*", "+", "/", "(", ")", "^"]
    s = s.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in symbol:
            tokens.append(s)
            i += 1

        elif "0" <= s[i] <= "9":
            num = ""
            while i < len(s) and "0" <= s[i] <= "9":
                num += s[i]
                i += 1
            tokens.append(num)

        else:
            return []

        return tokens


def main():
    exp = input("Enter a mathematical expression: ")
    tokens = token_list(exp)
    print(f"The token are: {tokens}")


if __name__ == '__main__':
    main()

