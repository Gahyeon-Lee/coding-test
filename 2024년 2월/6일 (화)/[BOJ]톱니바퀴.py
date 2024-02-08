# 14891.py
# 톱니바퀴

from collections import deque

def left(num, direct):
    # 첫번째 톱니는 확인하지 않음
    if num < 0:
        return
    # 같은 극이 아니면 회전
    if graph[num][2] != graph[num + 1][6]:
        left(num - 1, -direct)
        graph[num].rotate(direct)
        
def right(num, direct):
    # 마지막 톱니는 확인 안함
    if num > 3:
        return
    # 같은 극이 아니면 회전
    if graph[num - 1][2] != graph[num][6]:
        right(num + 1, -direct)
        graph[num].rotate(direct)

graph = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    num, direct = map(int, input().split())
    num -= 1
    # -d인 이유는 회전할 톱니번호가 회전하는 방향의 반대방향으로 회전해야 하기 때문
    left(num - 1, -direct)
    right(num + 1, -direct)
    
    graph[num].rotate(direct)

score = 0
for i in range(4):
    if graph[i][0] == 1:
        score += 2 ** i

print(score)