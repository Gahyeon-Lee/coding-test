# 7576.py
# 토마토

from collections import deque

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs()
count = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    count = max(count, max(i))
print(count - 1)