# 11724.py
# 연결 요소의 개수

import sys
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

result = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1
print(result)    