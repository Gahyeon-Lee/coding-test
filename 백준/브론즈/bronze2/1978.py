# 1978.py
# 소수 찾기

n = int(input())
nums = list(map(int, input().split()))

count = 0
prime = 0
for i in nums:
    if i == 1:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            
    if count == 2:
        prime += 1
    count = 0

print(prime)