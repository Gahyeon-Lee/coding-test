# 문자열 재정렬
# 난이도: 1 | 풀이 시간: 20분 | 시간 제한: 1초 | 메모리 제한: 128MB

n = input()

num = 0
string = ""
for i in n:
    if i.isdigit() == True:
        num += int(i)
    else:
        string += i

new_s = sorted(string)
print("".join(new_s) + str(num))


# 다음은 해설지의 답
# 숫자값이 0일 때 예외를 설정하지 못했다! 근데 문제가 세세하게 나온 게 아니어서 문제가 더 구체적이었다면...
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))