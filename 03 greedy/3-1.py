# 3-1.py
# 거스름돈

money = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += money // coin
    money %= coin
    
print(count)