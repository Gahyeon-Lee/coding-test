# 15650.py
# N과 M (2)

n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if (len(s) == 0 or s[-1] < i) and i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()


# 또 다른 풀이를 찾았다. 이게 더 깔끔하다. 그리고 이해도 더 쉽다.
def dfs_2(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(v, n + 1):
        if i not in s:
            s.append(i)
            dfs_2(i + 1)
            s.pop()

# dfs_2(1)