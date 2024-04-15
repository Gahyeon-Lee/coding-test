# 2667.py
# 단지번호붙이기

from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    count += 1
                    q.append((nx, ny))
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
            