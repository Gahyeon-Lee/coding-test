# 1919.py
# 애너그램 만들기

a = list(input())
b = list(input())

a.sort()
b.sort()

count = 0
for i in range(len(a)):
    if a.count(a[i]) != b.count(b[i]):
        count += 1

print(count)