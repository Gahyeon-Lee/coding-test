# 3-5.py
# 1이 될 때까지


# 내가 푼 거 (정답은 맞는데 모든 케이스에 대하여 맞는지 확신 없음)
n, k = map(int, input().split())

count = 0
while n > 1:
    if n % k == 0:
        n //= k
    else: 
        n -= 1
    count += 1
 
print(count)

# 교재
"""n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
    
while n > 1:
    n -= 1
    result += 1

print(result)"""