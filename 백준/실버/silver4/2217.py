# 2217.py
# 로프

# 문제점: 문제가 이해가 안 된다 ^^ (shit..)
# 정리를 좀 해야겠다

n = int(input())

weight = []
for _ in range(n):
    weight.append(int(input()))

weight.sort()

answers = []
for x in weight:
    answers.append(x * n)
    n -= 1
print(max(answers))