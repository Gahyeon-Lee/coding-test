# 문자열 뒤집기 두 번째 풀어보기

# 교재 답하고는 약간 다른데 그래도 전체적인 풀이 방법은 같다.
# 교재 답이 좀 더 느낌이 살긴 한다. 전문가 같다고 해야 할까. (두근두근)
# 암튼 풀긴 했다. 머리가 많이 발전한 느낌이 나서 기분이 좋은데 문제가 쉬운 거여서 그런 거다. (단호)

s = list(input())

group0 = 0
group1 = 0

now = s[0]

for i in range(1, len(s)):
    if now != s[i]:
        if now == '0':
            group0 += 1
        else:
            group1 += 1
        now = s[i]

# 본인은 이렇게 작성했는데
if group0 > group1:
    print(group1)
else:
    print(group0)
    
# 이렇게 줄일 수 있다. 하지만 맨날 까먹는다. ㅎㅎ
print(min(group0, group1))