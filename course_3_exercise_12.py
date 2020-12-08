s = "3ab14c2CaB"
s_2 = list()
s_3 = list()

i = 0
while i < len(s):
    if s[i].isdecimal():
        j = i
        while s[j].isdecimal():
            j += 1
        s_2.append(s[i:j])
        i = j
    else:
        s_2.append(s[i])
        i += 1
print(s_2)

i = 0
while i < len(s_2):
    if s_2[i].isdecimal():
        s_3.append(s_2[i + 1] * int(s_2[i]))
    else:
        s_3.append(s_2[i])
        i -= 1
    i += 2

[print(*el, end="", sep="") for el in s_3]
