# EXERCISE 102 : Check password


def check_password(pw):
    has_upper = False
    has_lower = False
    has_num = False

    for char in pw:
        if "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "1" <= char <= "9":
            has_num = True

    if len(pw) >= 8 and has_upper and has_lower and has_num:
        return True


def main():
    pw = input("Enter your pw: ")
    if check_password(pw):
        print(f"The pw {pw} is a good password")
    else:
        print(f"The pw {pw} is not a good password")


if __name__ == '__main__':
    main()
