# EXERCISE 104 : Hexadecimal and decimal digits

def hex2int(h):
    if h.isdigit():
        if 0 <= int(h) <= 9:
            i = int(h)
        return i
    
    h = h.upper()
    if h == 'A':
        i = 10
    elif h == 'B':
        i = 11
    elif h == 'C':
        i = 12
    elif h == 'D':
        i = 13
    elif h == 'E':
        i = 14
    elif h == 'F':
        i = 15
    else:
        return f"{h} is not a hexadecimal"
    return i


def int2hex(i):
    if 0 <= i <= 9:
        h = integer
        return h
    elif 10 <= i <= 15:
        if i == 10:
            h = 'A'
        elif i == 11:
            h = 'B'
        elif i == 12:
            h = 'C'
        elif i == 13:
            h = 'D'
        elif i == 14:
            h = 'E'
        else:
            h = 'F'
        return h
    else:
        return f"No hexadecimal corresponding to {i}"


if __name__ == '__main__':
    hexa = input('Enter hexadecimal: ')
    print(hex2int(hexa))
    print()
    integer = int(input('Enter integer: '))
    print(int2hex(integer))

