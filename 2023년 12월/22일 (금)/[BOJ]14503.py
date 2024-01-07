# 14503.py
# 로봇 청소기

from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, d):
    q = deque()
    q.append((x, y, d))
    graph[x][y] = 2
    count = 1
    
    while q:
        x, y, d = q.popleft()
        temp_d = d
        turn_time = 0
        
        for _ in range(4):
            nd = (temp_d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            temp_d = nd
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny, nd))
                    count += 1
                    break
                else:
                    turn_time += 1
        
        if turn_time == 4:
            bx = x + dx[(d + 2) % 4]
            by = y + dy[(d + 2) % 4]
            
            if graph[bx][by] == 0:
                q.append((bx, by, d))
            else:
                return count
            
print(bfs(r, c, d))