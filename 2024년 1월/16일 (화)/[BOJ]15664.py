# 15664.py
# N과 M (10)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n
s = []

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    flag = 0
    for i in range(v, n):
        if not visited[i] and flag != numbers[i]:
            visited[i] = True
            s.append(numbers[i])
            flag = numbers[i]
            dfs(i + 1)
            s.pop()
            visited[i] = False
dfs(0)