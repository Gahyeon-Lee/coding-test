# 14503.py
# 로봇 청소기

from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
count = 0

visited = [[0] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate_clockwise():
    global d
    d -= 1
    if d == -1:
        d = 3

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    global count
    count += 1
    
    while q:
        x, y = q.popleft()
        turn_time = 0
        
        rotate_clockwise()
        nx = x + dx[d]
        ny = y + dy[d]
            
        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny))
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1
        
        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            
            if graph[nx][ny] == 0:
                q.append((nx, ny))
            else:
                break
            turn_time = 0
    
bfs(r, c)
print(count)