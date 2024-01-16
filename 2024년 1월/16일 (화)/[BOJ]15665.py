# 15665.py
# N과 M (11)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    flag = 0
    for i in range(n):
        if flag != numbers[i]:
            s.append(numbers[i])
            flag = numbers[i]
            dfs()
            s.pop()

dfs()