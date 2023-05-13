# 1697.py
# 숨바꼭질

from collections import deque

def bfs(v):
    q = deque([v])
    
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx) 
                
n, k = map(int, input().split())
MAX = 100001
dist = [0] * (MAX)

print(bfs(n))