# 2606.py
# 바이러스

from collections import deque

n = int(input())
pair = int(input())

computer = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(pair):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)
        
def bfs(graph, v):
    global count 
    queue = deque([v])

    while queue:
        now = queue.popleft()
        visited[now] = True
        
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                count += 1
    
    print(count)

bfs(computer, 1)