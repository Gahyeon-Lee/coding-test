# 1541.py
# 잃어버린 괄호

# 다시 풀어봐도 좋을 듯한 문제!! 좋은 로직인 것 같다.
formula = input().split('-')

expression = []

for num in formula:
    sum_value = 0
    
    temp = num.split('+')
    
    for i in temp:
        sum_value += int(i)
    expression.append(sum_value)

for i in range(1, len(expression)):
    expression[0] -= expression[i]

print(expression[0])