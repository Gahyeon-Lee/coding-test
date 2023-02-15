# 3-6.py
# 1이 될 때까지 (더 효율적인 방법)

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k
    
result += (n - 1)
print(result)