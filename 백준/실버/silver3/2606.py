# 2606.py
# 바이러스

n = int(input())
m = int(input())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())    # 연결을 양방향으로 해야 함. 단방향으로 해서 틀렸음!!!!
    data[a].append(b)  
    data[b].append(a)

def dfs(start):
    visited[start] = 1
    
    for i in data[start]:
        if visited[i] == 0:
            dfs(i)
            
visited = [0] * (n + 1)
dfs(1)

print(sum(visited) - 1)