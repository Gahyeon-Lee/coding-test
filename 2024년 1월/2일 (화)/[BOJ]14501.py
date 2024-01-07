# 14501.py
# 퇴사

n = int(input())

dp = [0] * (n + 1)
schedule = []
for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))
    
for i in range(n):
    for j in range(i + schedule[i][0], n + 1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])