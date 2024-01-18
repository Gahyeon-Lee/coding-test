# 10026.py
# 적록색약

import sys
sys.setrecursionlimit(1000000)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input())))

visited = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, color):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, graph[nx][ny])

rgb, rb = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            rgb += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            rb += 1
            
print(rgb, rb)