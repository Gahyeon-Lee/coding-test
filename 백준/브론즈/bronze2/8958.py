# 8958.py
# OX 퀴즈

n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for i in ox_list:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)