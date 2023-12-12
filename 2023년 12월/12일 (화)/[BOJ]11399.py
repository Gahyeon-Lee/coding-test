# 11399.py
# ATM

n = int(input())
times = list(map(int, input().split()))

times.sort()

value = 0
answer = 0
for time in times:
    value += time
    answer += value

print(answer)