# 만들 수 없는 금액 두 번째 풀어보기

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    if target < x:
        break
    target += x

print(target)