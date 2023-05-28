# 1546.py
# 평균

n = int(input())
scores = list(map(int, input().split()))

m = max(scores)
total = 0
for score in scores:
    total += (score / m * 100)

print(total / n)