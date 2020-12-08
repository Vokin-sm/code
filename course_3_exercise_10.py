a = "abc"
b = "d"
index_set = set()

if b in a:
    for i in range(len(a)):
        if a.find(b, i, len(a)) != -1:
            index_set.add(a.find(b, i, len(a)))
else:
    print(-1)

print(*sorted(list(index_set)))