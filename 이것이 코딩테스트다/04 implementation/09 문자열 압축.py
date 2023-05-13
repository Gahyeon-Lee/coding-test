# 문자열 압축
# 난이도: 1.5 | 풀이 시간: 30분 | 시간 제한: 1초 | 메모리 제한: 128MB

# https://programmers.co.kr/learn/courses/30/lessons/60057
# 위의 사이트에 가서 풀어야 한다고 함


def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
                
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer