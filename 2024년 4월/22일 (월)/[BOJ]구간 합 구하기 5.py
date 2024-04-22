# 11660.py
# 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
part = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        part[i][j] = part[i][j - 1] + part[i - 1][j] - part[i - 1][j - 1] + data[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = part[x2][y2] - part[x2][y1 - 1] - part[x1 - 1][y2] + part[x1 - 1][y1 - 1]
    print(result)