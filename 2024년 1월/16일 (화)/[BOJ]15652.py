# 15652.py
# N과 M (4)

n, m = map(int, input().split())
s = []

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(v, n + 1):
        s.append(i)
        dfs(i)
        s.pop()
        
dfs(1)