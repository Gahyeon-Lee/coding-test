# 11286.py
# 절대값 힙

import heapq
import sys

n = int(input())

q = []
for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(num), num))  # tuple로 구성했을 때 맨 앞 숫자만 가지고 정렬