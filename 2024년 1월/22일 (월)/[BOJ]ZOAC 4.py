# 23971.py
# ZOAC 4

h, w, n, m = map(int, input().split())

n = n + 1
m = m + 1

if h % n == 0:
    h //= n
else:
    h //= n
    h += 1

if w % m == 0:
    w //= m
else:
    w //= m
    w += 1
    
print(h * w)