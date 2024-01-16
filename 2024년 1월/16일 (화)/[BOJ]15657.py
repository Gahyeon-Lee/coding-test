# 15657.py
# N과 M (8)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in numbers:
        if len(s) == 0 or s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()
            
def other(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(v, n):
        s.append(numbers[i])
        other(i)
        s.pop()
            
dfs()
#other(0)