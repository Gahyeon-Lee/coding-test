# 1697.py
# 숨바꼭질

from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [0] * (MAX)

def bfs(v):
    q = deque()
    q.append(v)
    
    while q:
        now = q.popleft()
        
        if now == k:
            return dist[now]
        for nx in (now - 1, now + 1, now * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[now] + 1
                q.append(nx)
                
print(bfs(n))