# 10813.py
# 공 바꾸기

n, m = map(int, input().split())

nums = []
for i in range(n + 1):
    nums.append(i)

for i in range(m):
    a, b = map(int, input().split())
    nums[a], nums[b] = nums[b], nums[a]

for i in range(1, len(nums)):
    print(nums[i], end=' ')