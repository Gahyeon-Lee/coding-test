# 14215.py
# 세 막대

a, b, c = map(int, input().split())

first = max(a, b, c)
count = 0
while first >= (a + b + c - max(a, b, c)):
    first -= 1
    count += 1

print(a + b + c - count)