from itertools import groupby

s = "aaabccccCCaB"

for i, j in groupby(s):
    print(i, list(j))


"""s_2 = list()
s_3 = list()

if len(s) == 1:
    s_2.append(s)
else:
    i = 0
    while i < len(s)-1:
        j = i
        while s[i] == s[j]:
            j += 1
            if j == len(s):
                break
        s_2.append(s[i:j])
        i = j
        if i == len(s) - 1:
            s_2.append(s[-1:])

print(s_2)

for el in s_2:
    if len(el) == 1:
        s_3.append(el)
    else:
        s_3.append(str(len(el)) + el[0])

[print(*el, end="", sep="") for el in s_3]"""
