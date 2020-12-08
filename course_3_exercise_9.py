n, m = 4, 4
field = ["..*.",
         "**..",
         "..*.",
         "...."]

for i in range(n):
    field[i] = list(field[i].replace(".", "0"))

[print(el) for el in field]
print()


def minesweeper(a, b):
    global field
    field_d = [[a, b + 1], [a, b - 1], [a - 1, b - 1], [a - 1, b],
               [a - 1, b + 1], [a + 1, b], [a + 1, b - 1], [a + 1, b + 1]]
    for el_s in field_d:
        if 0 <= el_s[0] <= n - 1 and 0 <= el_s[1] <= m - 1 and field[el_s[0]][el_s[1]] != "*":
            field[el_s[0]][el_s[1]] = str(int(field[el_s[0]][el_s[1]]) + 1)


for i in range(n):
    for j in range(m):
        if field[i][j] == "*":
            minesweeper(i, j)

[print(*el, sep="") for el in field]













