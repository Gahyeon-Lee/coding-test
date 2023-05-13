# 10989.py
# 수 정렬하기 3

import sys

n = int(input())

num_list = [0] * 100001
for i in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(100001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)