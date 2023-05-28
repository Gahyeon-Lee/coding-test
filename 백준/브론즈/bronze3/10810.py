# 10810.py
# 공 넣기

n, m, = map(int, input().split())

basket = [0] * (n + 1)
for _ in range(m):
    i, j, k = list(map(int, input().split()))
    for row in range(i, j + 1):
        basket[row] = k
    
for i in range(1, len(basket)):
    print(basket[i], end=' ')