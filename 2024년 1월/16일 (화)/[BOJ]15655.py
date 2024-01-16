# 15655.py
# N과 M (6)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in numbers:
        if  (len(s) == 0 or s[-1] < i) and i not in s:
            s.append(i)
            dfs()
            s.pop()

def other(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(v, n):
        if  numbers[i] not in s:
            s.append(numbers[i])
            other(i + 1)
            s.pop()
            
dfs()
# other(0)