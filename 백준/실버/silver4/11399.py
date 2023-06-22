# 11399.py
# ATM

n = int(input())
p = list(map(int, input().split()))

p.sort()
time = []

total = 0
for i in p:
    total += i
    time.append(total)

# [이렇게 풀어보자!]
# answer = 0
# for x in range(1, n+1):
#    answer += sum(peoples[0:x])

print(sum(time))