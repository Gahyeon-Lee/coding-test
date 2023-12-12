# 13305.py
# 주유소

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
answer = 0

for i in range(n - 1):
    if min_price > price[i]:
        min_price = price[i]
        
    answer += min_price * length[i]

print(answer)