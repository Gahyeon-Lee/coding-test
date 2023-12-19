# 문자열 압축 두 번째 다시 풀어보기

def solution(s):
    result = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        new = ""
        first = s[0:i]
        count = 1
    
        for j in range(i, len(s), i):
            if s[j : j + i] == first:
                count += 1
            else:
                new += str(count) + first if count >= 2 else first
                count = 1
                first = s[j : j + i]
                
        new += str(count) + first if count >= 2 else first
        result = min(result, len(new))
    return result

s = "aabbaccc"
print(solution(s))