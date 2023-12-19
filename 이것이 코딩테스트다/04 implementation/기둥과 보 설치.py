# 기둥과 보 설치
# 난이도 1.5 | 풀이 시간 50분 | 시간 제한 5초 | 메모리 제한 128MB

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x  - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, stuff, operate = frame
        
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
        
    return sorted(answer)
        
    """ if frame[2] == 1 and frame[3] == 1:
            if data[x][y] == 0 or data[x][y + 1] == 1 or data[x + 1][y] == 1:
                data[x][y] = 1
            else:
                continue
        elif frame[2] == 1 and frame[3] == 0:
            if data[x][y] == 1:
                data[x][y] = 0
            else:
                continue
        elif frame[2] == 0 and frame[3] == 1:
            if data[x + 1][y] == 0 or (data[x - 1][y] == 1 and data[x + 1][y] == 1):
                data[x][y] = 2
            else:
                continue
        else:
            if data[x][y] == 1:
                data[x][y] = 0
            else:
                continue"""
    

n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], 
#               [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(n, build_frame)) # n은 좌표 크기 (n x n)