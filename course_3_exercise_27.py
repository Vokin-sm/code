n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input().split())

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()
