n = int(input())

for n in range(14):
    for k in range(13):
        for m in range(12):
            if 28*n + 30*k + 31*m == 365:
                print(n, k, m)