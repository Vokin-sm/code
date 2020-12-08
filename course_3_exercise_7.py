import math

s = "4".split()
s_2 = []

for i in range(1, len(s)):
    s_2.append(int(math.fabs(int(s[i - 1]) - int(s[i]))))

if sorted(s_2) == [i for i in range(1, len(s))]:
    print("Jolly")
else:
    print("Not jolly")
