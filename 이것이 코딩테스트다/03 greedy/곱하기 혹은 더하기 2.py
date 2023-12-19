# 곱하기 혹은 더하기 두 번째 풀어보기

s = input()

result = 0
for i in s:
    num = int(i)
    
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)