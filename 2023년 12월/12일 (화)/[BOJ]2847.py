# 2847.py
# 게임을 만든 동준이

n = int(input())

points = []
for _ in range(n):
    points.append(int(input()))
    
points = points[::-1]

answer = 0
for i in range(n - 1):
    while points[i] <= points[i + 1]:
        points[i + 1] -= 1
        answer += 1

print(answer)