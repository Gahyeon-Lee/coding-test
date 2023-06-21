# 1417.py
# 국회의원 선거

import heapq

n = int(input())
win = int(input())

vote = []
count = 0

for _ in range(n - 1):
    num = int(input())
    heapq.heappush(vote, (-num, num))

while vote:
    num = heapq.heappop(vote)[1]
    if num >= win:
        num -= 1
        win += 1
        count += 1
        heapq.heappush(vote, (-num, num))
print(count)