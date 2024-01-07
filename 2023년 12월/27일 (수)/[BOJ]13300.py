# 13300.py
# 방 배정

n, k = map(int, input().split())

student = [[0, 0] for _ in range(7)]
for i in range(n):
    s, y = map(int, input().split())
    student[y][s] += 1

rooms = 0
for i in range(1, 7):
    for j in range(0, 2):
        if student[i][j] % k != 0:
            rooms += student[i][j] // k + 1
        else:
            rooms += student[i][j] // k

print(rooms)