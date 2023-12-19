# 볼링공 고르지 두 번째 풀어보기

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if data[i] != data[j]:
            count += 1

print(count)


"------------답안지-------------"
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n
    
print(result)