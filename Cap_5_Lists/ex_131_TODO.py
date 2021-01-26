
symbol = ["*", "+", "/", "(", ")", "^"]
operators = []
postfix = []


def infix_to_postfix(infix):
    for t in infix:
        if t.is_integer():
            postfix.append(t)

        if t in symbol:
            while len(operators) != 0:
                if operators[-1] != "(":