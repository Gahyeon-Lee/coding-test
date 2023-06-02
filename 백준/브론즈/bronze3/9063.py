# 9063.py
# 대지

n = int(input())

x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

h = max(x) - min(x)
v = max(y) - min(y)

print(h * v)