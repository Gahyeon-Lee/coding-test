# 곱하기 혹은 더하기

s = input()

result = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    if num < 2 or result < 2:
        result += num
    else:
        result *= num
print(result)

# '0' 혹은 '1' 인 경우 더하기  -> 1의 경우를 빼먹음!!!!
# '2' 이상인 경우 곱하기