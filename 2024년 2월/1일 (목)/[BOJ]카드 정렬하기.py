# 1715.py
# 카드 정렬하기

import heapq, sys
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    heapq.heappush(q, int(input()))

total = 0
while len(q) > 1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    sum_value = x + y
    total += sum_value
    
    heapq.heappush(q, sum_value)
print(total)