# 14500.py
# 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

max_value = max(map(max, graph)) 
result = 0

def dfs(x, y, idx, total):
    global result
    
    if result >= total + max_value * (3 - idx):
        return
    
    if idx == 3:
        result = max(result, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if idx == 1:
                    visited[nx][ny] = True
                    dfs(x, y, idx + 1,total + graph[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, idx + 1, total + graph[nx][ny])
                visited[nx][ny] = False
            
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

print(result)