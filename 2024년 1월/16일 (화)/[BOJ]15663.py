# 15663.py
# N과 M (9) 
# 여기서부터 중요해짐!!!

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    flag = 0
    for i in range(n):
        if not visited[i] and flag != numbers[i]:
            visited[i] = True
            s.append(numbers[i])
            flag = numbers[i]
            dfs()
            visited[i] = False
            s.pop()

dfs()