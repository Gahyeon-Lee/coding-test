# 5585.py
# 거스름돈

coins = [500, 100, 50, 10, 5, 1]
count = []

n = int(input())
money = 1000 - n

for coin in coins:
    count.append(money // coin)
    money %= coin

print(sum(count))