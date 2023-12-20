# 5014.py
# 스타트링크

from collections import deque

# F층, 현재 S층, 스타트링크 G층, Up and Down
f, s, g, u, d = map(int, input().split())

stair = [0] * (f + 1)
visited = [0] * (f + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        now = q.popleft()
        
        if now == g:
            return stair[g]
        for i in (now + u, now - d):
            if 1 <= i <= f and not visited[i]:
                visited[i] = 1
                stair[i] = stair[now] + 1
                q.append(i)
                
    if stair[g] == 0:
        return "use the stairs"
            
print(bfs(s))