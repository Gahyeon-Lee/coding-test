# 9-3.py
# 플로이드 워셜 알고리즘

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 얻니는 경우에 쓰임
# 모든 지점의 최단 거리 정보를 갈무리 하기 위해 2차원 리스트에 갈무리 -> O(n^2)
# 총 시간 복잡도는 O(n^3)
# 다이나믹 프로그래밍에 속함

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()