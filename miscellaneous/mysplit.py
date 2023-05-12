def mysplit(strng):
    lst = []

    if len(strng) > 0:
        strng += ' '

    s = ''
    for ch in strng:
        if ch == ' ':
            if len(s) > 0:
                lst.append(s.strip())
            s = ''
        else:
            s += ch
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
