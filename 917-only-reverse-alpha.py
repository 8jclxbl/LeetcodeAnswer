def reverseOnlyLetters(S):
    temp = [i for i in S]
    length = len(temp)
    idx = [0 for i in range(length)]
    reg = []

    for i in range(length):
        asc = ord(temp[i])
        if 64 < asc < 91 or 96 < asc < 123:
            reg.append(temp[i])
            idx[i] = 1

    for i in range(length):
        if idx[i] == 1:
            temp[i] = reg.pop()

    return ''.join(temp)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))