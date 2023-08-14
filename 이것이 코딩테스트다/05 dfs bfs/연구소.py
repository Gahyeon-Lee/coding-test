# 연구소
# 난이도 2 | 풀이 시간 40분 | 시간 제한 2초 | 메모리 제한 512MB

n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range (n):
    data.append(list(map(int, input().split())))
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

reuslt = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[ny][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
                
    return score

def dfs(count):
    global reuslt
    
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        # 각 바이러스의 위치에서 전파 진행 
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(reuslt)