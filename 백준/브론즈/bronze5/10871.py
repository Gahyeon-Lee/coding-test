# 10871.py
# X보다 작은 수

n, x = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
    if num < x:
        print(num, end=' ')