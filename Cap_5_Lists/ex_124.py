# EXERCISE 124 - Line of Best Fit
# TODO

from statistics import mean

x_list = []
y_list = []

X = input("Enter the value of x (blank to quit): ")
Y = input("Enter the value of y: ")

while X != "":
    x = float(X)
    y = float(Y)

    x_list.append(x)
    y_list.append(y)

    X = input("Enter the value of x (blank to quit): ")
    if X == "":
        break
    Y = input("Enter the value of y: ")


def best_fit_line(xs, ys):
    m = (mean(xs) * mean(ys)) / mean(xs) * mean(ys) - mean(xs * xs)
    b = mean(ys) - m * mean(xs)

    return m, b


print(x_list)
print(y_list)

result = best_fit_line(x_list, y_list)

print(result)
