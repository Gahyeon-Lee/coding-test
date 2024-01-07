# 14889.py
# 스타트와 링크

import itertools

n = int(input())

graph = []
for _ in range(n):
    s = graph.append(list(map(int, input().split())))

arr = [i for i in range(1, n + 1)]
arr = list(itertools.combinations(arr, n // 2))

min_value = 1e5

for i in range(len(arr) // 2):
    start = arr[i]
    link = arr[len(arr) - i - 1]
    
    start_total = 0
    for i in start:
        for j in start:
            start_total += graph[i - 1][j - 1]
            
    link_total = 0
    for i in link:
        for j in link:
            link_total += graph[i - 1][j - 1]
            
    diff = abs(start_total - link_total)
    min_value = min(min_value, diff)

print(min_value)