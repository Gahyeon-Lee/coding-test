# 14499.py
# 주사위 굴리기

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(direction, x, y):
    global dice
    
    if direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        
    if graph[x][y] == 0:
        graph[x][y] = dice[-1]
    else:
        dice[-1] = graph[x][y]
        graph[x][y] = 0

for i in command:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]
    
    if 0 <= nx < n and 0 <= ny < m:
        turn(i, nx, ny)
        print(dice[0])
        x, y, = nx, ny