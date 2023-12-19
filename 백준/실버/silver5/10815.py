# 10815.py
# 숫자 카드

n = int(input())
got = list(map(int, input().split()))

m = int(input())
yesornot = list(map(int, input().split()))

result = {}

for i in yesornot:
    result[i] = 0

for i in got:
    if i in result:
        result[i] = 1
        
for i in result.values():
    print(i, end=' ')