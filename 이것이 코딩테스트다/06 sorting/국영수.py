# 국영수
# 난이도 1 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 256MB

n = int(input())

data = []
for _ in range(n):
    info = input().split()
    data.append((info[0], int(info[1]), int(info[2]), int(info[3])))
    
data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in data:
    print(student[0])
    
    
"=============================="
"아래는 교재 정답"

n = int(input())

data = []
for _ in range(n):
    data.append(input().split())
    
data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in data:
    print(student[0])