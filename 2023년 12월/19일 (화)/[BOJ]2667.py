# 2667.py
# 단지번호붙이기

from collections import deque

n = int(input())

result = []
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
    result.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            
result.sort()

print(len(result))
for i in result:
    print(i)