# 3-2.py
# 큰 수의 법칙

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

#1. 내가 푼 거

max_value = max(data)
data.remove(max_value)

sum_max = 0
for i in range(m // k):
    for _ in range(k):
        sum_max += max_value
    sum_max += max(data)

if m % k > 0:
    sum_max += max_value * (m % k)
    
print(sum_max)

# 2. 교재 1 (M이 100억만큼 커지면 시간 초과 남)

""" data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result) """

# 3. 교재 2 (시간 초가 안 나는 코드)
data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k  # 가장 큰 수가 등장하는 회수
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)