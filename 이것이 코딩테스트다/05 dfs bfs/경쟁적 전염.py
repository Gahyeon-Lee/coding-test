#  경쟁적 전염
# 난이도 2 | 풀이 시간 50분 | 시간 제한 1초 | 메모리 제한 256MB

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(n):
        # 해당 위치에 비이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 낮은 번호의 바이러스부터 증식하니까 정렬 먼저 하고 큐에 담기            
data.sort()
q = deque(data)
    
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 위, 오른, 왼, 아래
# 북,  동,  남,  서

while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
     
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
            
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))
                    
        
print(graph[target_x - 1][target_y - 1])


# s를 어떻게 이용해야 하는가
# 어떻게 한 번씩만 반복을 돌릴 것인가