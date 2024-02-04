# 2108.py
# 통계학

import sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    q.append(int(input()))
q.sort()

print(round(sum(q) / n))
print(q[len(q) // 2])

count = dict()
for i in q:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
frequency = max(count.values())
number = []

for key, value in count.items():
    if value == frequency:
        number.append(key)

if len(number) == 1:
    print(number[0])
else:
    print(sorted(number)[1])

print(abs(max(q) - min(q)))