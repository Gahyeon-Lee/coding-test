# 10816.py
# 숫자 카드 2

n = int(input())
card = list(map(int, input().split()))

m = int(input())
other = list(map(int, input().split()))

total = {}

for i in card:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1

for i in other:
    if i in total:
        print(total[i], end=' ')
    else:
        print(0, end=' ')