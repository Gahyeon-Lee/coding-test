# 15656.py
# N과 M (7)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in numbers:
        s.append(i)
        dfs()
        s.pop()

dfs()