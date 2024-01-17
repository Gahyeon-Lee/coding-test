# 14502.py
# 연구소

from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스가 퍼지는 함수
def bfs():
    q = deque()
    temp = copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))
    global answer
    count = 0

    for i in range(n):
        count += temp[i].count(0)
    answer = max(answer, count)
        
# 벽을 세우는 함수
def make_wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0
                
make_wall(0)
print(answer)