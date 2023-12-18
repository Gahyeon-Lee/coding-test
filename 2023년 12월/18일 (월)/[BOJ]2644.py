# 2644.py
# 촌수계산

from collections import deque
 
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(v):
    queue = deque([v])
    visited[v] = 0
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)

bfs(a)

if visited[b]:
    print(visited[b])
else:
    print(-1)