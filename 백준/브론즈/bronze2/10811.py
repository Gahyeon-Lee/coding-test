# 10811.py
# 바구니 뒤집기

n, m = map(int, input().split())

basket = []
for i in range(n + 1):
    basket.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i:j+1]
    temp.reverse()
    basket[i:j+1] = temp
    
for i in range(1, len(basket)):
    print(basket[i], end=' ')
    