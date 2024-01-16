# 15666.py
# N과 M (12)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    flag = 0
    for i in range(v, n):
        if flag != numbers[i]:
            s.append(numbers[i])
            flag = numbers[i]
            dfs(i)
            s.pop()

dfs(0)