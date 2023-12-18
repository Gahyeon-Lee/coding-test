# 1260.py
# DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

visited = [0] * (n + 1)
visited2 = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[now][i] == 1:
                visited2[i] = 1
                queue.append(i)

dfs(v)
print()
bfs(v)