# 15903.py
# 카드 합체 놀이

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

#i = 0
#while i != m:
#    data.sort()
#    a = data.pop(0)
#    b = data.pop(0)
    
#    result = a + b
#    data.append(result)
#    data.append(result)
#    i += 1

#print(sum(data))

heap = []
for i in data:
    heapq.heappush(heap, i)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a + b)

print(sum(heap))