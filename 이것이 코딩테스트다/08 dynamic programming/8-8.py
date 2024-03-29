# 8-8.py
# 효율적인 화폐 구성

n, m = map(int, input().split())

array = []
for i in range(n):
    num = int(input())
    array.append(num)

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])