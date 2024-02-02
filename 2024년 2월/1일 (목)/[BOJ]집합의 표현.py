# 1717.py
# 집합의 표현

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    num, a, b = map(int, input().split())
    
    if num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')