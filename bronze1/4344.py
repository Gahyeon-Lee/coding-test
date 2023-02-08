# 4344.py
# 평균은 넘겠지

import sys

c = int(input())

for _ in range(c):
    n = list(map(int, sys.stdin.readline().split()))
    average = sum(n[1:]) // n[0]
    count = 0
    for i in n[1:]:
        if i > average:
            count += 1
    print("%.3f" % (count / n[0] * 100) + "%")