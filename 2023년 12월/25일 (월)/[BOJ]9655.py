# 9655.py
# 돌 게임

n = int(input())

d = [-1] * 1001
d[1] = 1
d[2] = 0
d[3] = 1

for i in range(4, n + 1):
    if d[i - 1] == 1 or d[i - 3] == 1:
        d[i] = 0
    else:
        d[i] = 1

if d[n] == 1:
    print('SK')
else:
    print('CY')

# 인터넷에서 본 풀이법
# 즉 n-1 or n-3이 이미 존재한다면 그 결과의 반대가 나오게 된다.
# 따라서 n-1이나 n-3의 결과를 반대로 저장해주면 된다.