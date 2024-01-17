# 1251.py
# 단어 나누기

s = input()

answer = []
for i in range(len(s) - 2):
    a = list(s[:i + 1])
    for j in range(1, len(s) - 1):
        b = list(s[i + 1 : i + j + 1])
        c = list(s[i + j + 1:])
        
        result = ''
        
        if len(c) != 0:
            result = ''.join(a[::-1]) + ''.join(b[::-1]) + ''.join(c[::-1])
            answer.append(result)

answer.sort()
print(answer[0])


# 아니 나는 왜 이렇게 더럽게 코드가 나왔는지;;
# 일단 깔끔한 거는 참고하라고

"""
word = input()
ans_list = []
for i in range(1,len(word)-1):
	ans = []
	for j in range(i+1,len(word)):
		ans = ((word[0:i:])[::-1])+((word[i:j:])[::-1])+((word[j::])[::-1])
		ans_list.append(ans)

ans_list.sort()
print(ans_list[0])
"""