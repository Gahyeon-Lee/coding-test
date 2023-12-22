# 9205.py
# 맥주 마시면서 걸어가기

from collections import deque

def bfs():
    q = deque()
    q.append((start_x, start_y))
    
    while q:
        x, y = q.popleft()
        
        if abs(x - end_x) + abs(y - end_y) <= 1000:
            return 'happy'
        
        for i in range(n):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    
    return 'sad'

t = int(input())

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    end_x, end_y = map(int, input().split())
    
    visited = [0] * (n + 1)
    print(bfs())