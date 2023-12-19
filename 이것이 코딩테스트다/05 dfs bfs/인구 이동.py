# 인구 이동
# 난이도 2 | 풀이 시간 40분 | 시간 제한 2초 | 메모리 제한 512MB

from collections import deque

n, l, r = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    # (x, y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = data[x][y]
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and union[x][y] == -1:
                if l <= abs(data[ny][ny] - data[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += data[nx][ny]
                    count += 1
                    united.append((nx, ny))
    
    for i, j in united:
        data[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)