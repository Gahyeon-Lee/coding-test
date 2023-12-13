# 20300.py
# 서강 근육맨

n = int(input())
degree = list(map(int, input().split()))

degree.sort()

value = -1
if n % 2 == 0:
    for i in range(n // 2):
        value = max(degree[i] + degree[n - i - 1], value)
    print(value)
else:
    for i in range((n - 1) // 2):
        value = max(degree[i] + degree[n - i - 2], value)
    print(max(value, degree[-1]))