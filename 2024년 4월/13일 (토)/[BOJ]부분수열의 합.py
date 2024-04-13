# 1182.py
# 부분수열의 합

n, s = map(int, input().split())
part = list(map(int, input().split()))
count = 0

def dfs(value, idx):
    global count
    
    if idx >= n:
        return
    
    value += part[idx]
    
    if value == s:
        count += 1
    
    dfs(value, idx + 1)
    dfs(value - part[idx], idx + 1)

dfs(0, 0)
print(count)