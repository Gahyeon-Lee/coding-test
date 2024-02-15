# 1926.py
# 그림

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return count

max_value = 0
picture = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            picture += 1
            max_value = max(max_value, bfs(i, j))

print(picture)
print(max_value)