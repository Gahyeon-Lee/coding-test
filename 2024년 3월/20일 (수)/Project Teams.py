# 20044.py
# Project Teams

min_value = 10 ** 6

n = int(input())
abilities = list(map(int, input().split()))
abilities.sort()

for i in range(n * 2 // 2):
    sum_value = abilities[i] + abilities[n * 2 - i - 1]
    min_value = min(min_value, sum_value)

print(min_value)