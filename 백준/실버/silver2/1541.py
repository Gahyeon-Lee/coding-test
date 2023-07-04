# 1541.py
# 잃어버린 괄호

# +를 먼저 계산하고 그 다음 -를 계산하기
#  '-'를 기준으로 해서 괄호를 치면 된다
# '-'로 식을 나누면 숫자로만 구성되거나 숫자와 '+'로 구성된 문자열들이 생성
# 후에 각 문자열들을 다시 '+'를 기준으로 하여 split 하여 숫자만 남게 함
# 숫자들을 더해서 결과 값들을 다른 리스트에 저장

f = input().split('-')

num = []
for i in f:
    sum = 0
    temp = i.split('+')
    
    for j in temp:
        sum += int(j)
    num.append(sum)

first = num[0]

for i in range(1, len(num)):
    first -= num[i]
print(first)