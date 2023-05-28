# 3052.py
# 나머지

rests = []
for i in range(10):
    n = int(input())
    rest = n % 42
    rests.append(rest)

rests = list(set(rests))
print(len(rests))