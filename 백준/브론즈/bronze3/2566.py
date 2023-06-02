# 2566.py
# 최댓값

matrix = []
for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

maxNum = 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= maxNum:
            maxNum = matrix[i][j]
            a, b = i, j

print(maxNum)
print(a + 1, b + 1)