# 문자열 뒤집기

data = input()

result = 0
count = 0
zero_num = data.count('0')
one_num = data.count('1')

if zero_num > one_num:
    find = 1
else:
    find = 0

for i in data:
    if int(i) == find:
        count += 1
    else:
        if count > 0:
            result += 1
            count = 0
print(result)