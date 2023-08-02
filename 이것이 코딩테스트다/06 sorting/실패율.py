# 실패율
# 난이도 1 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB

def solution(N, stages):
    miss = []
    total = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if total == 0:
            prob = 0
        else:
            prob = count / total
        miss.append((i, prob))
        total -= count
        
    miss.sort(key=lambda x: (-x[1], x[0]))
    
    result = []
    for i in miss:
        result.append(i[0])
    return result