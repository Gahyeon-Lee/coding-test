# 약수

import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

print(nums[0] * nums[-1])