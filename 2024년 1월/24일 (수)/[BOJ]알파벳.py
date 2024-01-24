# 1987.py
# 알파벳

r, c = map(int, input().split())
graph = [input() for _ in range(r)]
visited = [0] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited[ord(graph[0][0]) - 65] = 1
count = 1

def dfs(x, y, result):
    global count
    count = max(count, result) 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[ord(graph[nx][ny]) - 65]:
                visited[ord(graph[nx][ny]) - 65] = 1
                dfs(nx, ny, result + 1)
                visited[ord(graph[nx][ny]) - 65] = 0

dfs(0, 0, 1)
print(count)