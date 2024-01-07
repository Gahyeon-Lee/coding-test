# 14889.py
# 스타트와 링크

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [0 for _ in range(n)]
min_value = 1e4

def dfs(depth, index):
    global min_value
    
    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        min_value = min(min_value, abs(start - link))
        return
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0
        
dfs(0, 0)
print(min_value)