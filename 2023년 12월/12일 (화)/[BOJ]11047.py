# 11047.py
# 동전 0

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

answer = 0
for coin in coins:
    share = k // coin
    
    if share > 0:
        answer += share
    k %= coin

print(answer)