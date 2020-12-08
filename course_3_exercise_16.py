s = "4 44 44 "
s_2 = set()

for el in s.split():
    if s.split().count(el) > 1:
        s_2.add(el)

print(*sorted(list(s_2)))