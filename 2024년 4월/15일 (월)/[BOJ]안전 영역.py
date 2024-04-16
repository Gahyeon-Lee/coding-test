# 2468.py
# 안전 영역

from collections import deque

n = int(input())

graph = []
height = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > height:   
            height = graph[i][j]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][nx] > height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

count = 0
for k in range(height):
    visited = [[False] * n for _ in range(n)]
    value = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                bfs(i, j, k)
                value += 1
        
        count = max(count, value)
        
print(count)