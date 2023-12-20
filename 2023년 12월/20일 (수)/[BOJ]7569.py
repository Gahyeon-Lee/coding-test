# 7569.py
# 토마토

import sys
from collections import deque

m, n, h = map(int, input().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, y, x = q.popleft()
        
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = 1
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

bfs()
complete = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                complete = True
            day = max(day, visited[i][j][k])
            
if complete:
    print(-1)
else:
    print(day)