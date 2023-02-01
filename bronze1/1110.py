# 더하기 사이클

n = int(input())
original = n
count = 0

while True:
    a = original // 10
    b = original % 10
    c = (a + b) % 10
    original = (b * 10) + c
    count += 1
    
    if n == original:
        break

print(count)

