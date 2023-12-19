# 블록 이동하기
# 난이도 3 | 풀이 시간 50분 | 시간 제한 1초 | 메모리 제한 128MB

from collections import deque

def rotate_clockwise(direction):
    if direction != 3:
        direction += 1
    else:
        direction = 0
    return direction

def rotate_counterclockwise(direction):
    if direction != 0:
        direction -= 1
    else:
        direction = 3

def solution(board):
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    
    
    
    return

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))