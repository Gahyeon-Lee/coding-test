# 괄호 변환
# 난이도 1 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB

stack = []

def right_bracket(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            else:
                count -= 1
    return True
    
def balanced_bracket(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
            
        if count == 0:
            return i
            
def solution(p):
    answer = ''
    if p == '':
        return answer
    
    index = balanced_bracket(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    if right_bracket(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
        
    return answer


# p = "(()())()"
p = ")("
# p = "()))((()"

print(solution(p))