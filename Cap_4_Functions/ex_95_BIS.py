# EXERCISE 95 : Capitalize it BIS


def capitalize(s):
    li = list(s)
    pos = 0
    while pos < len(li) and li[pos] == " ":
        pos += 1
    
    li[pos] = li[pos].upper()

    # set pos after first char
    pos += 1
    for char in range(pos, len(li)):
        if li[char] == "i" and (li[char-1] == " " or li[char+1] == " " or li[char+1] == "'"):
            li[char] = li[char].upper()
        elif li[char] == "." or li[char] == "?" or li[char] == "!":
            li[char+2] = li[char+2].upper()
    
    result = "".join(li)
    return result


test_case  = "   what time do i have to be there? what's the address? this time i'll try to be on time! i promise"
print(capitalize(test_case))