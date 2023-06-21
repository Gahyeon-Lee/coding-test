# 1927.py
# 최소 힙

import heapq
import sys

n = int(input())

q = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(q, num)
    else:
        if not q:
            print(0) 
        else:
            print(heapq.heappop(q))