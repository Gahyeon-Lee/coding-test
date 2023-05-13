# 2751.py
# 수 정렬하기 2

import sys

n = int(input())

nums = []
for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    
nums.sort()

for i in nums:
    print(i)