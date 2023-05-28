# 25304.py
# 영수증

x = int(input())
n = int(input())

total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += (a * b)

if total == x:
    print('Yes')
else:
    print('No')