# EXERCISE 51 : Roots of a quadratic function

print("This program calculates the real roots of a quadratic equation(if any).")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

discriminate = b**2 - 4*a*c

if discriminate < 0:
    print("This quadratic function has no real root.")
elif discriminate == 0:
    print("This quadratic function has one real root.")

    root = -b / 2*a

    print(f"Real root = {root}")

elif discriminate > 0:
    print("This quadratic function has two real roots.")

    root1 = -b + discriminate / 2*a
    root2 = -b - discriminate / 2*a

    print(f"Real roots = {root1} or {root2}")
