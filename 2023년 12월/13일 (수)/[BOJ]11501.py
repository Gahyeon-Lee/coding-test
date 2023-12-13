# 11501.py
# 주식

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    
    total = 0
    max_stock = stock[-1]
    
    for i in range(n - 1, -1, -1):
        if max_stock < stock[i]:
            max_stock = stock[i]
        total += max_stock - stock[i]
    
    print(total)