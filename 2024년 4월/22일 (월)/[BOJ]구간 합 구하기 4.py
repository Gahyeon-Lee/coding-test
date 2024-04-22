# 11659.py
# 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
part = [0]

for i in data:
    element = i + part[-1]
    part.append(element)

for _ in range(m):
    i, j = map(int, input().split())
    part_sum = part[j] - part[i - 1]
    print(part_sum)
