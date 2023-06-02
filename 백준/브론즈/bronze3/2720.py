# 2720.py
# 세탁소 사장 동혁

coins = [25, 10, 5, 1]

t = int(input())

for _ in range(t):
    c = int(input())
    
    for coin in coins:
        print(c // coin, end=' ')
        c %= coin
    print("")