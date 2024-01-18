# 1012.py
# 유기농 배추

import sys
sys.setrecursionlimit(10000)

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                result += 1
        
    print(result)                