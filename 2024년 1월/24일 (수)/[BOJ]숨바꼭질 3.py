# 13549.py
# 숨바꼭질 3

from collections import deque

n, k = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)

q = deque()
q.append(n)
dist[n] = 0
    
while q:
    x = q.popleft()
        
    if x == k:
        print(dist[x])
        break
    
    for nx in (x * 2, x - 1, x + 1):
        if 0 <= nx <= MAX and not dist[nx]:
            if nx == x * 2:
                dist[nx] = dist[x]
                q.append(nx)
            else:
                dist[nx] = dist[x] + 1
                q.append(nx)