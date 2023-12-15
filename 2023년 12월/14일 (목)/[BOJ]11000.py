# 11000.py
# 강의실 배정

import sys, heapq

input = sys.stdin.readline
n = int(input())

time = []
for _ in range(n):
    s, t = map(int,input().split())
    time.append([s, t])

time = sorted(time, key=lambda x:x[0])

q = []
heapq.heappush(q, time[0][1]) # 끝 나는 시간을 넣어 둠

for i in range(1, n):
    if time[i][0] < q[0]:
        heapq.heappush(q, time[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, time[i][1])
    
print(len(q))