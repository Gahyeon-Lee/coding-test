# 1931.py
# 회의실 배정

n = int(input())

time_table = []
for _ in range(n):
    start, end = map(int, input().split())
    time_table.append((start, end))
    
time_table = sorted(time_table, key=lambda x: (x[1], x[0]))

last_end = 0
count = 0

for start, end in time_table:
    if start >= last_end:
        count += 1
        last_end = end

print(count)