# 4963.py
# 섬의 개수

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    count += 1
                    q.append((nx, ny))
    return count

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    dx = [-1, 0, 1, 0, -1, 1, -1, 1]
    dy = [0, 1, 0, -1, -1, -1, 1, 1]
    
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    
    print(result)
